def program173():
    n, m, z = map(int, input().split())
    a = list()
    b = list()
    c = int(0)
    for i in range(z):
        a.append(0)
        b.append(0)
        if (i + 1) % n == 0:
            a[i] = 1
        if (i + 1) % m == 0:
            b[i] = 1
        if a[i] == b[i] == 1:
            c += 1
    print(c)