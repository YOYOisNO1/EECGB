def program2314():
    mp() lambda: map(int, input().split())
    r1, r2 = mp()
    c1, c2 = mp()
    d1, d2 = mp()
    b = -1
    for a in range(1, 10):
        b = r1-a
        c = c1-a
        d = d1-a
        if b < 0 or c < 0 or d < 0 or b > 9 or c > 9 or d > 9:
            continue
        if c + d == r2 and c + b == d2 and b + d == c2:
            break
    if b == -1:
        print -1
    else:
        print a, b
        print c, d