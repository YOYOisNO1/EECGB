def program1906():
    (x,y) = map(int, input().strip().split())
    
    if x > 0:
        a = [abs(x)+abs(y), 0]
    else:
        a = [(abs(x)+abs(y))*(-1), 0]
    if y > 0:
        b = [0, abs(x)+abs(y)]
    else:
        b = [0, (abs(x)+abs(y))*(-1)]
    
    if a[0] < b[0]:
        print(' ').join(str(g) for g in (a+b))
    else:
        print(' ').join(str(g) for g in (b+a))