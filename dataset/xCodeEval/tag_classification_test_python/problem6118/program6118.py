def MinSteps(SourceX, SourceY, DestX, DestY):
        print(max(abs(SourceX - DestX), abs(SourceY - DestY)))
    
    r1, c1, r2, c2 = map(int, input().split())
    #For the Rook.
    if r1 == r2 or c1 == c2:
        rook = 1
    else:
        rook = 2
    
    #for bishop along right back
    i, j = r1, c1
    result = False
    bishop = 2
    while i > 0 and j > 0:
        if (i, j) == (r2, c2):
            bishop = 1
            result = True
            break
        j -= 1
        i -= 1
    if result:
        bishop = 1
    else:
        #for bishop along right forward
        i, j = r1, c1
        while i <= 8 and j <= 8:
            if (i, j) == (r2, c2):
                bishop = 1
                result = True
                break
            i += 1
            j += 1
        if result:
            bishop = 1
        else:
            #for bishop along left backward
            i, j = r1, c1
            while i > 0 and j <= 8:
                if (i, j) == (r2, c2):
                    bishop = 1
                    result = True
                    break
                i -= 1
                j += 1
            if result:
                bishop = 1
            else:
                #for bishop along left forward
                i, j = r1, c1
                while i <= 8 and j > 0:
                    if (i, j) == (r2, c2):
                        result = True
                        break
                    i += 1
                    j -= 1
                if result:
                    bishop = 1
    if (r1+c1)%2 != (r2+c2)%2:
        bishop = 0
    
    print(rook, bishop, end=" ")
    MinSteps(r1, c1, r2, c2)