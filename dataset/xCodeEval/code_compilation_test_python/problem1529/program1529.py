def program1529():
    #!/usr/bin/python
    
    
    import sys
    
    (r1, c1, r2, c2) = [int(a) for a in input().split()]
    
    if r1 > r2:
        r = r1 - r2
    else:
        r = r2 - r1
    
    if c1 > c2:
        c = c1 -c2
    else:
        c = c2 -c1
    
    
    ### Rook ###
    
    if r1 == r2:
        rook = 1
    elif c1 == c2:
        rook = 1
    else:
        rook = 2
    
    
    ##Bishop###
    if r1 == r2 or c1 == c2:
        bishop = 0
    else:
        if r == c:
            bishop = 1
        else:
            bishop = 2
    
    
    ###King###
    
    if r == c:
        king = r
    elif r>c:
        king = r
    else:
        king = c
    
    #Printing
    print rook, bishop, king     
    
    