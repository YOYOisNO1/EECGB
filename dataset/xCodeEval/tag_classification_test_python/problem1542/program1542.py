def program1542():
    p, d = map(int, input().split())
    pow10, res = 10, p
    while p >= pow10 - 1:
        c = (p % pow10 + 1) % pow10
        if c <= d:
            res = p - c
        pow10 *= 10
    print(res)