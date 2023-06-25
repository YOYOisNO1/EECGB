def program6123():
    r1,c1,r2,c2 = list(map(int,input().split()))
    if r1 == r2 or c1 == c2:
        ladia=1
        if r1 == r2:
            king = abs(c1-c2)
        elif c1 == c2:
            king = abs(r1-r2)
    else:
        ladia=2
        king=max(abs(r1-r2),abs(c1-c2))
    if (r1 % 2 == 1 and c1 % 2 == 1) or (r1 % 2 == 0 and c1 % 2 == 0):
        color1="black"
    else:
        color1="white"
    if (r2 % 2 == 1 and c2 % 2 == 1) or (r2 % 2 == 0 and c2 % 2 == 0):
        color2="black"
    else:
        color2="white"
    if color1 == color2:
        if abs(r1-r2) == abs(c1-c2):
            slon=1
        else:
            slon=2
    else:
        slon=0
    print(ladia,slon,king)