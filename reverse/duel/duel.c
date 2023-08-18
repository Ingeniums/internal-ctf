#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TOTAL_GAMES 100
#define MAX_RAND 100 

void win() {
    FILE *file = fopen("flag.txt", "r");
    printf("Congrats\n");
    if (file == NULL) {
        printf("Couldn't open flag file\n");
        exit(1);
    }

    char flag[100];
    if (fgets(flag, sizeof(flag), file) == NULL) {
        printf("Couldn't read flag\n");
        exit(1);
    }

    printf("Here is your flag: %s\n", flag);

    fclose(file);
}

int main() {
    srand(time(0)+0xdeadbeef+(3<<4)); 

    printf("To get the flag you need to win this duel\n");
    fflush(stdout);
    int player_wins = 0;

    for (int game = 1; game <= TOTAL_GAMES; game++) {
        int player_number, correct_num;

        printf("round #%d. your input: ", game);
        fflush(stdout);
        scanf("%d", &player_number);

        correct_num = rand() % MAX_RAND;

        if (player_number == correct_num) {
            player_wins++;
        }
        if (game != 0x64) {
            printf("Score:\n Bot: %d You: %d\n", game, player_wins);
        } else {
            printf("Score:\n Bot: 99 You: %d\n", player_wins);
        }
    }
    

    if (player_wins == TOTAL_GAMES) {
        win();
    } else {
        printf("Don't give up, try harder!\n");
    }

    return 0;
}
