from pwn import *
from ctypes import CDLL

libc = CDLL("/usr/lib64/libc.so.6")

libc.srand(libc.time(0)+0xdeadbeef+(3<<4))


# p = process("./duel")
p = remote("0.0.0.0", 1338)

for i in range(100):
    input = libc.rand()
    input = str(input % 100).encode()
    p.write(input+b'\n')
    print(p.clean().decode())

