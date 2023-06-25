def program6187():
    r1, c1, r2, c2 = map(int, input().split())
    x, y = abs(r1-r2), abs(c1-c2)
    if x==0 and y==0:
        print(0,) 0, 0
    else:
        k = max(x, y)
        r = 1 if (x==0 or y==0) else 2
        if x==y:
            b = 1
        elif (x+y)&1:
            b = 0
        else:
            b = 2
        print(r,) b, k