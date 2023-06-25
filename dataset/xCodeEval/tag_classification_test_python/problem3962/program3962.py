def program3962():
    w, m = map(int, input().split())
    s = 0
    p = 1
    for i in range(101):
        s += p
        p *= w
    m += s
    bad = False
    while m > 0:
        if m % w > 2:
            bad = True
        m //= w
    if bad:
        print('NO')
    else:
        print('YES')