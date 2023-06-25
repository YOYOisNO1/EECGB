def program6152():
    r1,c1,r2,c2 = map(int,input().split())
    rook = 0
    biop = 0
    king = 0
    if r1 == r2 and c1 == c2:
        print("0 0 0")
    else:
        if(r1 == r2 or c1 == c2):
            rook = 1
        else:
            rook = 2
        k1 = (r1 + c1) % 2
        k2 = (r2 + c2) % 2
        d1 = abs(r1 - r2)
        d2 = abs(c1 - c2)
        if(k1 == k2):
            if d1 == d2:
                biop = 1
            else:
                biop = 2
        king = max(d1,d2)
        print(str(rook) + " " + str(biop) + " " + str(king))