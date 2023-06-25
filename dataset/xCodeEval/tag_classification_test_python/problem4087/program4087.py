def program4087():
    R = lambda: map(int, input().split())
    n = int(input())
    l, r = 1, n
    while l < r:
        m = (l + r) // 2
        nc, vc = n, 0
        while nc > 0:
            vc += min(m, nc)
            nc -= min(m, nc)
            nc -= nc // 10
        if vc * 2 >= n:
            r = m
        else:
            l = m + 1
    print(l)