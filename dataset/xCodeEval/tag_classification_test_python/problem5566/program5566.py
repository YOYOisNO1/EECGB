def program5566():
    n, m = map(int, input().split())
    a = [0] * m
    i = []
    nn = n
    c = 0
    while nn > 0:
        nn -= 1
        i.append(c)
        c += 1
        if c == m:
            c = 0
    for x in i:
        a[x] += 1
    print(*a)