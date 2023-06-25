def program3921():
    w, m = map(int, input().split())
    while m > 1:
        c = m % w
        if c not in {0, 1, w - 1}:
            print('NO')
            exit()
        m //= w
        if c == w - 1:
            m += 1
    print('YES')