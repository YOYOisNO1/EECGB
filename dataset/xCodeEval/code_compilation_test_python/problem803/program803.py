def c(n, k)
        r = 1
        for j in range(1, k+1):
            r = r * (n - k + j)
        for j in range(1, k+1):
            r = r / j
        return r
            
    
    n,m,k = map(int,input().split())
    a = 0
    for i in range(1,k+1):
        if (i <= m && k - i <= n && k - i >= 4):
            a += c(k - i, n) * c(i, m)
    print a