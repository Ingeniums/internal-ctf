#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MAX_PASSWORDS 10

bool is_admin = false;

static char *passwords[MAX_PASSWORDS];

void disable_buffering(void) {
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
}

void menu() {
  puts("----- menu -----");
  puts("1. create password");
  puts("2. print password");
  puts("3. delete password");
  puts("4. change admin's password");
  puts("5. exit");
}

void do_create(void) {
  unsigned int index;
  size_t size;

  printf("index: ");
  scanf("%u", &index);

  if (index >= MAX_PASSWORDS) {
    puts("Nope.");
    return;
  }

  printf("size: ");
  scanf("%lu", &size);

  passwords[index] = malloc(size);

  printf("password: ");
  read(0, passwords[index], size);

  puts("Added!");
}

void do_print(void) {
  unsigned int index;

  printf("index: ");
  scanf("%u", &index);

  if (index >= MAX_PASSWORDS) {
    puts("Nope.");
    return;
  }

  if (passwords[index] == NULL)
    puts("No passwords here.");
  else
    printf("%s\n", passwords[index]);
}

void do_delete(void) {
  unsigned int index;

  printf("index: ");
  scanf("%u", &index);

  if (index >= MAX_PASSWORDS) {
    puts("Nope.");
    return;
  }

  free(passwords[index]);
}

void do_edit(void) {
  char buffer[16];
  printf("password: ");
  gets(buffer);
  puts("Edited!");
}

int main(int argc, char *argv[]) {
  disable_buffering();
  int choice = -1;

  while (choice != 5) {
    menu();
    printf("> ");
    scanf("%d", &choice);
    getchar();
    switch (choice) {
    case 1:
      do_create();
      break;
    case 2:
      do_print();
      break;
    case 3:
      do_delete();
      break;
    case 4:
      if (is_admin)
        do_edit();
      else
        puts("only an admin can do that!");
      break;
    default:
      break;
    }
  }
}
