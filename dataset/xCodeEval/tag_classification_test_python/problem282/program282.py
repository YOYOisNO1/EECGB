def program282():
    n, k = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    b = []
    c = []
    for i in range(n):
        if a[i] not in b:
            b.append(a[i])
            c.append(i + 1)
        if len(c) == k:
            break
    if len(c) >= k:
        print('YES')
        print(*c)
    else:
        print('NO')