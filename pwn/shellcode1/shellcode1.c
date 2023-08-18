#include <stdio.h>
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
    bye_function();
}

int main(int argc, char **argv) {
    char name[60];
    puts("May I have your name?");
    fflush(stdout);
    fgets(name, sizeof(name), stdin);
    srand(time(0));

    if (rand() % 2) hello(name, bye1);
    else hello(bye2, name);

    return 0;
}
//gcc -z execstack shellcode1.c -o elf
