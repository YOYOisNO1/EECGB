def program957():
    x,y = (int(i) for i in input().split(" "))
    u,v = (int(i) for i in input().split(" "))
    w,z = (int(i) for i in input().split(" "))
    
    xs = sorted([x,u,w])
    ys = sorted([y,v,z])
    
    mx = 0
    if xs[0] == xs[1] or xs[1] == xs[2]:
        if xs[0] == xs[1] and xs[1] == xs[2]:
            mx = 2
        else:
            mx = 1
    
    my = 0
    if ys[0] == ys[1] or ys[1] == ys[2]:
        if ys[0] == ys[1] and ys[1] == ys[2]:
            my = 2
        else:
            my = 1
    
    if mx == 2 or my == 2:
        print(1)
        exit(0)
    elif mx == 1:
        ok = True
        if x == u:
            if min(y,v) < z < max(y,v):
                ok = False
        elif x == w:
            if min(y,z) < v < max(y,z):
                ok = False
        elif u == w:
            if min(v,z) < y < max(v,z):
                ok = False
    elif my == 1:
        ok = True
        if y == v:
            if min(x,u) < w < max(x,u):
                ok = False
        elif y == z:
            if min(x,w) < u < max(x,w):
                ok = False
        elif v == z:
            if min(u,w) < x < max(u,w):
                ok = False
    else:
        ok = False
    
    
    print(2) if ok else 3