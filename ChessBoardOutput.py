import ChessBoardFunctions

n, m = raw_input("How big do you want the board (n,m)>2:").split()
n=int(n)
m=int(m)

board = [[' ' for _ in range(m)] for _ in range(n)]

ChessBoardFunctions.printBothNoReturn(board,n,m)

while True:
    piece, r, c = raw_input("Enter the piece followed by the colum and row (piece r c):").split()
    r=int(r) - 1
    c=int(c) - 1
    board = ChessBoardFunctions.placeChess(board,n,m,piece,r,c)
    ChessBoardFunctions.printBothWithReturn(board,n,m)
