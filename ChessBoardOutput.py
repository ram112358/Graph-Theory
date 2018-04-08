import sys

def printOneBoard(board,n,m):
    sys.stdout.write(" ")
    for i in range (0,m):
        sys.stdout.write("%2s" % (i+1))
    print("")
    for i in range (0,2*n+1):
        if (i%2 == 1):
            sys.stdout.write("%s" % (i/2+1))
        else:
            sys.stdout.write(" ")
        for j in range (0,2*m+1):
            if (i%2 == 0):
                sys.stdout.write("-")
            elif (j % 2 == 0):
                sys.stdout.write("|")
            else:
                sys.stdout.write(board[i/2][j/2])
        print("")
def printNineBoards(board,n,m):
    for _ in range (0,3):
        sys.stdout.write(" ")
        for i in range (0,m):
            sys.stdout.write("%2s" % (i+1))
    print("")
    for _ in range (0,3):
        for i in range (0,2*n+1):
            if (i%2 == 1):
                sys.stdout.write("%s" % (i/2+1))
            else:
                sys.stdout.write(" ")
            for _ in range (0,3):
                for j in range (0,2*m+1):
                    if (i%2 == 0):
                        sys.stdout.write("-")
                    elif (j % 2 == 0):
                        sys.stdout.write("|")
                    else:
                        sys.stdout.write(board[i/2][j/2])
            print("")
def placePiece(piece,n,m)


n, m = raw_input("How big do you want the board (two numbers:n m): ").split(' ')
n=int(n)
m=int(m)

board = [[' '] * m] * n

printOneBoard(board,n,m)
printNineBoards(board,n,m)
