def program6972():
    n, p = map(float, input().split())
    ans, n = 0, int(n)
    all = n * (n - 1) * (n - 2) // 6
    
    for i in range(n):
        deln, newp = n - i, 0
        if i > 2:
            newp += i * (i - 1) * (i - 2) // 6
        if i > 1:
            newp += deln * i * (i - 1) // 2
        if deln > 1:
            newp += deln * (deln - 1) * i / 4
    
        if newp / all >= p:
            break
        ans += 1
    
    print(ans)