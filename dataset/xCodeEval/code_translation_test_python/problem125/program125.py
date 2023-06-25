def program125():
    n, m, z = map(int, input().split())
    c = [int(i) for i in range(n, z+1, n)]
    a = [int(i) for i in range(m, z+1, m)]
    t = 0
    for i in c:
        if i in a:
            t += 1
    print(t)