def program3321():
    a,b,c = map(int, input().split())
    if max(a,b,c) == a:
        k = a - (b+c)
        if k < 0:
            print(0)
        else:
            print(k+1)
    elif max(a,b,c) == b:
        l = b - (a+c)
        if l < 0:
            print(0)
        else:
            print(l + 1)
    elif max(a,b,c) == c:
        m = c - (a+b)
        if m < 0:
            print(0)
        else:
            print(m+1)