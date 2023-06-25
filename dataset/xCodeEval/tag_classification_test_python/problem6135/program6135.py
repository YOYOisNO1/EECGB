def program6135():
    r1, c1, r2, c2 = (int(s) for s in input().split())
    
    print((1) if r1 == r2 or c1 == c2 else 2), (1 if abs (r1 - r2) == abs (c1 - c2) else 2 * ((r1 + r2 + c1 + c2 + 1) % 2)), max (abs (r1 - r2), abs (c1 - c2))