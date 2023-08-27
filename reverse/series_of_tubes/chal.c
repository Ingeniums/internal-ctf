#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

#define INPUT_LEN 32

unsigned char TARGET[] = {
    0x2d, 0x29, 0x31, 0x34, 0x2c, 0x32, 0x27, 0x30, 0x2b, 0x24, 0x4c,
    0x39, 0x6f, 0x44, 0x73, 0x37, 0x32, 0x74, 0x36, 0x3b, 0x77, 0x57,
    0x4d, 0x8c, 0x71, 0x50, 0x79, 0x3f, 0x3d, 0x50, 0x69, 0x38,
};

unsigned char buffer[INPUT_LEN];
int tubes[3][2];

int main(void) {
  read(0, buffer, INPUT_LEN);
  pipe(tubes[0]);

  int pid = fork();

  if (pid == 0) {
    read(tubes[0][0], buffer, INPUT_LEN);

    for (int i = 0; i < INPUT_LEN; i++)
      buffer[i] ^= 0xff;

    write(tubes[0][1], buffer, INPUT_LEN);
    exit(0);
  }

  write(tubes[0][1], buffer, INPUT_LEN);
  waitpid(pid, NULL, 0);
  read(tubes[0][0], buffer, INPUT_LEN);

  pipe(tubes[1]);
  pid = fork();

  if (pid == 0) {
    read(tubes[1][0], buffer, INPUT_LEN);

    for (int i = 0; i < INPUT_LEN; i++)
      buffer[i] = (buffer[i] - 0x69) % 256;

    write(tubes[1][1], buffer, INPUT_LEN);
    exit(0);
  }

  write(tubes[1][1], buffer, INPUT_LEN);
  waitpid(pid, NULL, 0);
  read(tubes[1][0], buffer, INPUT_LEN);

  pipe(tubes[2]);
  pid = fork();

  if (pid == 0) {
    read(tubes[2][0], buffer, INPUT_LEN);

    for (int i = 1; i < INPUT_LEN; i++)
      buffer[i] = (buffer[i] + i) % 256;

    write(tubes[2][1], buffer, INPUT_LEN);
    exit(0);
  }

  write(tubes[2][1], buffer, INPUT_LEN);
  waitpid(pid, NULL, 0);
  read(tubes[2][0], buffer, INPUT_LEN);

  if (memcmp(buffer, TARGET, 32) == 0)
    puts("you got it");
  else
    puts("nope");
}
