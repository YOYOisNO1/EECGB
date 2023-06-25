def program2030():
    n, k, d  = [int(x) for x in input().split()]
    
    mod = 1e9+7
    
    a = [[None for _ in range(2)] for _ in range(n+1)]
    
    a[0][0] = 1
    a[0][1] = 0
    for i in range(1, n + 1):
        a[i][0] = 0
        a[i][1] = 0
        for j in range(1, k + 1):
            if j > i:
                break
            if j < d:
                a[i][0] = (a[i][0] + a[i - j][0]) % mod
            else:
                # print(i-j, a[i - j][0])
                a[i][1] = (a[i][1] + a[i - j][0]) % mod
            a[i][1] = (a[i][1] + a[i - j][1]) % mod
    
    # print(a)
    print(int(a[n][1]))