def program1721():
    x, y, m = map(int, input().split())
    
    if x>y:
        x, y = y, x
    
    if y>=m:
        print(0)
    elif y<=0:
        print(-1)
    else:
        k = 0
        if x<0:
            k = -x/y+1
            x = x%y
            if not x:
                x += y
        while y<m:
            x, y = y, x+y
            k += 1
        print(k)