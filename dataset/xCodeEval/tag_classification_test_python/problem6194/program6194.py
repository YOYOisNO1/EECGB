def program6194():
    r1, c1, r2, c2 = map(int, input().split())
    b = 0
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        b = 1 + (r1 - c1 != r2 - c2 and r1 + c1 != r2 + c2)
    print((r1 != r2) + (c1 != c2), b, max(abs(r1 - r2), abs(c1 - c2)))