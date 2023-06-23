def program3854():
    (r, h) = map(int, input().split())
    
    s = 0
    s += h / r * 2
    
    if h - (h / r) * r >= r/2.:
        s += 2
    else:
        s += 1
    
    print s