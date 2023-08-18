#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void disable_buffering(void) {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

void vuln(void) {

  char name[128];
  puts("The floor is yours.\n");

  while (1) {

    printf("Please enter your name: ");

    fgets(name, 127, stdin);

    name[strcspn(name, "\n")] = 0;

    if (!strncmp(name, "exit", 4)) {
      puts("I mean, sure.");
      return;
    }

    printf("Welcome, ");
    printf(name);
    printf(".\n");
  }
}

int main(void) {
  disable_buffering();
  vuln();
  return 0;
}
