def program2366():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    P = []
    for i in range(n):
        P.append((a[i], i))
    P = sorted(P, reverse=True)
    for i in range(n):
        k = a[i] // 2 + int(a[i] % 2 != 0)
        b[i] += k
        w -= k
    
    if w < 0:
        print(-1)
        exit()
    
    i = 0
    while w > 0:
        k = a[P[i][1]] - b[P[i][1]]
        b[P[i][1]] += min(w, k)
        w -= min(w, k)
        i += 1
    
    print(*b)