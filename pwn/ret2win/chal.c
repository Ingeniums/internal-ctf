#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void disable_buffering(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

void VerY_s3cREt_fUnCti0N() {
  char flag[64];

  FILE *f = fopen("./flag.txt", "r");
  if (f == NULL) {
    puts("Something has gone terribly wrong, please contact an admin.");
    exit(-1);
  }

  int size = fread(flag, 1, 63, f);
  flag[size] = 0;
  printf("DING DING DING! here is your flag: %s\n", flag);
}

void vuln(void) {

  char name[32];
  puts("Welcome to my greeting service!\n");

  while (1) {

    printf("Please enter your name: ");

    gets(name);

    if (!strncmp(name, "exit", 4)) {
      puts("I mean, sure.");
      return;
    }

    printf("Welcome, ");
    printf(name);
    printf("!\n");
  }
}

int main(void) {
  disable_buffering();
  vuln();
  return 0;
}
