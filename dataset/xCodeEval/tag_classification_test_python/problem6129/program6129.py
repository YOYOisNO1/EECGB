    import os,sys
    ###Rook, Bishop and King: 370A http://codeforces.com/problemset/problem/370/A
    
    ###Little Petya is learning to play chess. He has already learned how to move a king, a rook and a bishop. Let us remind you the rules of moving chess pieces. A chessboard is 64 square fields organized into an 8*8 table. A field is represented by a pair of integers (r,c)-the number of the row and the number of the column (in a classical game the columns are traditionally indexed by letters). Each chess piece takes up exactly one field. To make a move is to move a chess piece, the pieces move by the following rules:
    
    ###input
    #The input contains four integers r1,c1,r2,c2,the coordinates of the starting and the final field. The starting field doesn't coincide with the final one.
    
    ###output
    #Print three space-separated integers: the minimum number of moves the rook, the bishop and the king (in this order) is needed to move from field (r1,c1) to field (r2,c2). If a piece cannot make such a move, print(a) 0 instead of the corresponding number.
    
def run():
        x1, y1, x2, y2 = map(int, input().split())
        if x1==x2 and y1==y2:
            print(0,) 0, 0
            return
        king = 0
        rook = 0
        bishop = 0
        if x1==x2 or y1==y2:
            rook = 1
        else:
            rook = 2
        if abs(x1-y1)%2 == abs(x2-y2)%2:
            if abs(x1-x2) == abs(y1-y2):
                bishop = 1
            else:
                bishop = 2
        king = max(abs(x1-x2), abs(y1-y2))
        print(rook,) bishop, king
        return
    #################################################
    run()