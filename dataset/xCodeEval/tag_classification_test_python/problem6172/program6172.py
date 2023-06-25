def program6172():
    r1, c1, r2, c2 = (int(s) for s in input().split())
    
    r, b, k = 0, 0, 0
    
    if r1 == r2 or c1 == c2:
        r = 1
    else:
        r = 2
    
    if abs (r1 - r2) == abs (c1 - c2):
        b = 1
    elif (r1 + r2 + c1 + c2) % 2 == 0:
        b = 2
    else:
        b = 0
    
    k = max (abs (r1 - r2), abs (c1 - c2))
    
    print(r,) b, k