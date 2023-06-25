def program615():
    import fractions
    
    n, m, x, y, a, b = [int(i) for i in input().strip().split()]
    
    g = fractions.gcd(a, b)
    if g != 1:
       a /= g
       b /= g
    
    h = n / a
    v = m / b
    scale = min(h, v)
    h = a * scale
    v = b * scale
    
    bottomleftx = 0
    bottomlefty = 0
    toprightx = 0
    toprighty = 0
    
    if h % 2 == 1:
        bottomleftx = x - (h+1)/2
    else:
        bottomleftx = x - h/2
    if bottomleftx < 0:
        bottomleftx = 0
    toprightx = bottomleftx + h
    
    rightx = x + h/2
    if rightx > n:
        toprightx = n
        bottomleftx = n - h
    
    if v % 2 == 1:
        bottomlefty = y - (v+1)/2
    else:
        bottomlefty = y - v/2
    if bottomlefty < 0:
        bottomlefty = 0
    toprighty = bottomlefty + v
    
    topy = y + v/2
    if topy > m:
        toprighty = m
        bottomlefty = m - v
    
    print(bottomleftx,) bottomlefty, toprightx, toprighty