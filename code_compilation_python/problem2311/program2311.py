def program2311():
    r1,r2 = map(int,input().split())
    c1,c2 = map(int,input().split())
    d1,d2 = map(int,input().split())
    y = (d2+(r2-c2))//2
    x = d2-y
    w = r1-x
    z = d1-w
    if not 1<w<20 or not 1<x<20 not 1<y<20 or 1<z<20:
        print(-1)
        exit()
    if w != x and w != y and w != z and x != y and x != z and y != z:
        print(-1)
        exit()
    else:
        print(w,x)
        print(y,z)