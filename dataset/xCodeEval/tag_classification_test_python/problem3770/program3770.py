def program3770():
    
    a = map(int, input().split())
    b = map(int, input().split())
    c = map(int, input().split())
    d = map(int, input().split())
    
    
    ok = False
    
    if a[3]:
        if b[0] or c[1] or d[2] or a[0]or a[1] or a[2]:
            ok = True
    
    
    if b[3]:
        if c[0] or d[1] or a[2] or b[0]or b[1] or b[2]:
            ok = True
    
    
    if c[3]:
        if d[0] or a[1] or b[2] or c[0] or c[1] or c[2]:
            ok = True
    
    
    if d[3]:
        if a[0] or b[1] or c[2] or d[0]or d[1] or d[2]:
            ok = True
    
    if ok:
        print("YES")
    else:
        print("NO")