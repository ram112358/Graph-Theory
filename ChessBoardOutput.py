import ChessBoardFunctions

n, m = raw_input("How big do you want the board (two numbers:n m): ").split()
n=int(n)
m=int(m)

board = [[' ' for _ in range(m)] for _ in range(n)]

while True:
    ChessBoardFunctions.printOneBoard(board,n,m)
    ChessBoardFunctions.printNineBoards(board,n,m)
    piece, c, r = raw_input("Enter the piece followed by the colum and row (piece c r):").split()
    r=int(r) - 1
    c=int(c) - 1
    board = ChessBoardFunctions.placeChess(board,n,m,piece,r,c)
