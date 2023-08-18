#define _GNU_SOURCE
#include <stdio.h>
#include <unistd.h>
#include <seccomp.h>
#include <sys/syscall.h> 
#include <stdlib.h>
#include <time.h>

void bye1() {
    puts("Goodbye...");
}

void bye2() {
    puts("Farewell...");
}

void hello(char *name, void (*bye_function)()) {
    printf("Hello %s!\n", name);
    fflush(stdout);
    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(open), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
    seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
    seccomp_load(ctx);
    bye_function();
    seccomp_release(ctx);
}


int main(int argc, char **argv) {

    char name[100];
    puts("may i have your name?");
    fflush(stdout);
    fgets(name, sizeof(name), stdin);

    srand(time(0));
    if (rand() % 2) hello(name, bye1);
    else hello(bye2, name);

    
    return 0;
}
// sudo dnf install libseccomp-devel
// gcc -w -z execstack shellcode2.c -o elf -lseccomp
