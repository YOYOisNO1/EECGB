def program3995():
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
            print('NO')
            exit()
        m //= w
    print('YES')