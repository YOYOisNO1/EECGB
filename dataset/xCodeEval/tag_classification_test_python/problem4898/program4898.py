def program4898():
    
    n, p, w, d = [int(x) for x in input().split()]
    y = 0
    while y < w and p % w:
        y += 1
        p -= d
    x = p // w
    z = n - x - y
    if y == w or p < 0 or z < 0: print(-1)
    else: print(x, y, z)