# include <stdlib.h>
# include <stdio.h>
# define MAX_SECRETS 5

void disable_buffering() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL); 
    setbuf(stderr, NULL);
}

void menu() {
    puts("1/ add secret"); 
    puts("2/ edit secret"); 
    puts("3/ delete secret"); 
    puts("4/ consult secret");
    puts("5/ quit");
    puts("");
}

void win() {
    disable_buffering();
    FILE *file = fopen("flag.txt", "r");
    printf("GG here is your flag!\n");
    if (file == NULL) {
        printf("Couldn't open flag file\n");
        exit(1);
    }

    char flag[100];
    if (fgets(flag, sizeof(flag), file) == NULL) {
        printf("Couldn't read flag\n");
        exit(1);
    }

    printf("%s\n", flag);
    fclose(file);
}

// gcc chal.c -o elf -fstack-protector -Wl,-z,relro,-z,now

int main(int argc, char** argv) {
    disable_buffering();
    char * secrets[MAX_SECRETS] = {0};
    size_t secret_sizes[MAX_SECRETS] = {0};

    puts("welcome to my secret keeper!");
    puts("");
    printf("LEAK: your secrets are hidden at: %p\n", secrets);
    puts("");

    while (1)
    {
        menu();
        puts("");
        int choice;
        int index;
        size_t size;
        puts("input: \n");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("index: \n");
                scanf("%d", &index);


                if (index < 0 || index >= MAX_SECRETS) {
                    printf("Invalid index.\n");
                    exit(1);
                }

                printf("size: \n");
                scanf("%lu", &size);

                if (size <= 0) {
                    printf("Invalid size.\n");
                    exit(1);
                }
                void* secret = malloc(size);

                secret_sizes[index] = size;
                secrets[index] = secret;
                break;
            case 2:
                printf("index: \n");
                scanf("%d", &index);


                if (index < 0 || index >= MAX_SECRETS || secrets[index] == NULL) {
                    printf("Invalid index.\n");
                    exit(1);
                }
                size_t size = secret_sizes[index];
                printf("reading secret (up to %lu characters): \n", size);
                scanf(" ");
                fgets(secrets[index], size, stdin);
                break;
            case 3:
                printf("index: \n");
                scanf("%d", &index);


                if (index < 0 || index >= MAX_SECRETS || secrets[index] == NULL) {
                    printf("Invalid index.\n");
                    exit(1);
                }

                free(secrets[index]);
                break;
            case 4:
                printf("index: \n");
                scanf("%d", &index);


                if (index < 0 || index >= MAX_SECRETS || secrets[index] == NULL) {
                    printf("Invalid index.\n");
                    exit(1);
                }
                puts("secret content: ");
                puts(secrets[index]);
                break;
            case 5:
                return 0;
            default:
                printf("Unrecognized choice :(.\n");
                return 1;
        }
    }
    
}



