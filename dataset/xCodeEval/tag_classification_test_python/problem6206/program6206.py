def program6206():
    #Rook, Bishop and King
    # graph, maths, shortest path
    
    r1, c1, r2, c2 = map(int, input().split())
    # For Bishop
    Bishop = -1
    if((r1+c1) % 2 != (r2+c2) % 2):
        Bishop = 0
    elif(abs(r2-r1) == abs(c2-c1)):
        Bishop = 1
    else:
        Bishop = 2
    
    # For Rook
    
    Rook = -1
    if(r1==r2 or c1==c2):
        Rook = 1
    else:
        Rook = 2
    
    # For King
    
    King = max(abs(r1-r2),abs(c1-c2))
    print(Rook,Bishop,King)