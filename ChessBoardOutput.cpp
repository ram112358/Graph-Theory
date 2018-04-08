#include<iostream>
#include<stdio.h>

using namespace std;

void printBoard();

int n = 0;
char* piece;

int main(){
    cout << "n = ";
    cin >> n;

    char pieces[n][n] = {};
    piece = *pieces;

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            pieces[i][j] = ' ';
        }
    }



    // while (true){
        printBoard();
        cout << "What is the piece? (q to quit):";

        cout << "Where would you like to place a piece? (X):";
        cout << "Where would you like to plaec a piece? (Y):";
    // }
}

void printBoard(){
    for (int i = 0; i < 2*n + 1; i++){
        for (int j = 0; j < 2*n + 1; j++){
            if (i % 2 == 0)
                printf("-");
            else if (j % 2 == 0)
                printf("|");
            else
                cout << piece[i/2][j/2];
        }
    printf("\n");
    }
}
