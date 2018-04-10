import sys

def printBothWithReturn(board,n,m):
    for x in range(8*n + 5):
        sys.stdout.write("\033[F\033[K")
    printOneBoard(board,n,m)
    printNineBoards(board,n,m)

def printBothNoReturn(board,n,m):
    printOneBoard(board,n,m)
    printNineBoards(board,n,m)

def printOneBoard(board,n,m):
    sys.stdout.write(" ")
    for i in range (0,m):
        sys.stdout.write("%2s" % (i+1))

    print("")

    for i in range (0,2*n+1):
        if i%2 == 1:
            sys.stdout.write("%s" % (i/2+1))
        else:
            sys.stdout.write(" ")

        for j in range (0,2*m+1):
            if i%2 == 0 and j%2 == 0:
                sys.stdout.write("+")
            elif i%2 == 0:
                sys.stdout.write("-")
            elif j % 2 == 0:
                sys.stdout.write("|")
            else:
                sys.stdout.write(board[i/2][j/2])

        print("")

def printNineBoards(board,n,m):
    sys.stdout.write(" ")
    for i in range (0,3*m):
            sys.stdout.write("%2s" % ((i%3)+1))

    print("")

    for i in range (0,6*n+1):
        if i%2 == 1:
            sys.stdout.write("%s" % (i/2+1))
        else:
            sys.stdout.write(" ")

        for j in range (0,6*m+1):
            if i%2 == 0 and j%2 == 0:
                sys.stdout.write("+")
            elif i%2 == 0:
                sys.stdout.write("-")
            elif j%2 == 0:
                sys.stdout.write("|")
            else:
                sys.stdout.write(board[i/2%3][(j/2)%3])

        print("")

def limitPiece(n,m,r,c):
    if r >= n or r < 0:
        r = r%n
    if c >= m or c < 0:
        c = c%m
    return r , c

# checks if it's a chess piece and shows ownership markers, if not just places the peice
def placeChess(board,n,m,piece,r,c):
    if piece == "I":
        board = placePiece(board,n,m,piece,r,c)
        board = placePiece(board,n,m,"~",r+1,c+1)
        board = placePiece(board,n,m,"~",r+1,c-1)
        board = placePiece(board,n,m,"~",r+1,c  )
        board = placePiece(board,n,m,"~",r-1,c+1)
        board = placePiece(board,n,m,"~",r-1,c-1)
        board = placePiece(board,n,m,"~",r-1,c  )
        board = placePiece(board,n,m,"~",r  ,c+1)
        board = placePiece(board,n,m,"~",r  ,c-1)
    elif piece == "K":
        board = placePiece(board,n,m,piece,r,c)
        board = placePiece(board,n,m,"~",r+2,c+1)
        board = placePiece(board,n,m,"~",r+2,c-1)
        board = placePiece(board,n,m,"~",r-2,c+1)
        board = placePiece(board,n,m,"~",r-2,c-1)
        board = placePiece(board,n,m,"~",r+1,c+2)
        board = placePiece(board,n,m,"~",r-1,c+2)
        board = placePiece(board,n,m,"~",r+1,c-2)
        board = placePiece(board,n,m,"~",r-1,c-2)
    else:
        board = placePiece(board,n,m,piece,r,c)
    return board;

# uses limitPiece and then places the piece so long as it isn't filled
def placePiece(board,n,m,piece,r,c):
    r , c = limitPiece(n,m,r,c)
    if board[r][c] == " " or board[r][c] == "~":
        board[r][c] = piece
    return board;
