#include <stdio.h>
#include <string.h>
#include <unistd.h>

unsigned char SECRET[] = {0x17, 0x93, 0x91, 0x93, 0x97, 0x5d, 0x35, 0x86, 0x0d,
                          0x01, 0xa0, 0x5b, 0x19, 0x52, 0x0d, 0x09, 0xce, 0x52,
                          0x35, 0x5e, 0x0a, 0x09, 0xce, 0x4e, 0x13, 0x8b, 0x61,
                          0x18, 0x8a, 0x0e, 0x33, 0x84, 0x4d, 0x07, 0x8a, 0x57,
                          0x04, 0x9a, 0x59, 0x04, 0x96};

void xor_func(unsigned char *In, size_t len) {
  for (size_t i = 0; i < len; i++) {
    if (i % 3 == 2) {
      In[i] ^= 0x3e;
    } else if (i % 3 == 0) {
      In[i] ^= 0xff;
    } else {
      In[i] ^= 0x6a;
    }
  }
}

void rev(unsigned char *In, size_t len) {
  for (size_t i = 0; i < len / 2; i++) {
    unsigned char temp = In[i];
    In[i] = In[len - 1 - i];
    In[len - 1 - i] = temp;
  }
}

void swap(unsigned char *In) {
  unsigned char a = In[19];
  In[19] = In[3];
  In[3] = a;
  a = In[13];
  In[13] = In[2];
  In[2] = a;
}

void disable_buffering() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

int main() {
  disable_buffering();
  unsigned char input[41];
  printf("Enter passkey: ");
  read(0, input, 41);

  xor_func(input, 41);
  rev(input, 41);
  swap(input);

  if (memcmp(input, SECRET, 41) == 0) {
    printf("You win!\n");
  } else {
    printf("Wrong passkey :(\n");
  }

  return 0;
}
