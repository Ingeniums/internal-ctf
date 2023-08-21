BITS 64

section .text
global _start
_start:
  ; write prompt
  mov rax, 1
  mov rdi, 1
  mov rsi, prompt
  mov rdx, prompt_len
  syscall

  ; read input
  xor rax, rax
  xor rdi, rdi
  mov rsi, input
  mov rdx, 17
  syscall

  xor rbx, rbx


   mov cl, 0x6d
   call _check
   

   mov cl, 0x34
   call _check
   

   mov cl, 0x35
   call _check
   

   mov cl, 0x74
   call _check
   

   mov cl, 0x33
   call _check
   

   mov cl, 0x72
   call _check
   

   mov cl, 0x5f
   call _check
   

   mov cl, 0x34
   call _check
   

   mov cl, 0x35
   call _check
   

   mov cl, 0x73
   call _check
   

   mov cl, 0x33
   call _check
   

   mov cl, 0x6d
   call _check
   

   mov cl, 0x62
   call _check
   

   mov cl, 0x31
   call _check
   

   mov cl, 0x33
   call _check
   

   mov cl, 0x72
   call _check
   

   mov cl, 0x21
   call _check

  mov rax, 1
  mov rdi, 1
  mov rsi, correct
  mov rdx, correct_len
  syscall
  jmp _exit

_failed:
  mov rax, 1
  mov rdi, 1
  mov rsi, failed
  mov rdx, failed_len
  syscall

_exit:
  mov rax, 0x3c
  xor rdi, rdi
  syscall


_check:
 lea rax, [input+rbx]
 mov al, byte [rax]
 xor al, cl
 jnz _failed
 inc rbx
 ret
  

  
section .data
prompt: db 'Your input: ', 0
prompt_len: equ $ - prompt
failed: db `Wrong :(\n`, 0
failed_len: equ $ - failed
correct: db `Correct!\n`, 0
correct_len: equ $ - correct

section .bss
input: resb 18

; m45t3r_45s3mb13r!

