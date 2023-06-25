def program996():
    (a, b, c) = (int(x) for x in input().split())
    (x, y, z) = (int(x) for x in input().split())
    
    ra = 0
    rb = 0
    rc = 0
    rem = 0
    
    if a > x:
        ra = (a - x) / 2
    else:
        rem += (x - a)
    if b > y:
        rb = (b - y) / 2
    else:
        rem += (y - b)
    if c > z:
        rc = (c - z) / 2
    else:
        rem += (z - c)
    
    if rem <= ra + rb + rc:
        print('Yes')
    else:
        print('No')
    
    
    
    