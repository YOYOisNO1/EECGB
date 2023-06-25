def program2798():
    w, h = map(int , input().split() )
    u1, d1 = map(int , input().split() )
    u2, d2 = map(int , input().split() )
    while h!=0:
        w = w + h
        if h== d1:
            w = w - u1
        if h == d2:
            w = w-u2
        h =h -1
        w = max(0,w)
    print(w)