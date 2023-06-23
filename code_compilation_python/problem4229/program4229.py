def gcd(a, b):
        if a % b  == 0:
            return b
        else:
            return gcd(b, a%b)
    n, m, x, y, a, b = map(int, input().split())
    d = gcd(a, b)
    a = a/d
    b = b/d
    
    k = min(n/a, m/b)
    dx = k*a
    dy = k*b
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    
    if x-(dx/2+dx%2) <=0:
        x1 = 0
        x2 = dx
    else:
        x1 = x-(dx/2+dx%2)
        x2 = x+dx/2
    if y-(dy/2+dy%2) <=0:
        y1 = 0
        y2 = dy
    else:
        y1 = y-(dy/2+dy%2)
        y2 = y+dy/2
    
    print x1, y1, x2, y2
    