def program766():
    n, m = map(int, input().split())
    dc = 0
    a = 1
    while n > 0:
        dc += 1
        n -= 1
    
        if a*m == dc:
            n += 1
            a += 1
    
    print(dc)