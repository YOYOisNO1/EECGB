def program3788():
    n, l, r = map(int, input().split())
    m = 10 ** 9 + 7
    
    a = [0, 0, 0]
    
    a[l % 3] = (r - l + 1) / 3
    a[(l + 1) % 3] = (r - l + 1) / 3
    a[(l + 2) % 3] = (r - l + 1) / 3
    
    k = (r - l + 1) % 3
    if k == 1: a[l % 3] += 1
    if k == 2:
        a[l % 3] += 1
        a[(l + 1) % 3] += 1
    
    dp = [a[0], a[1], a[2]]
    for i in range(1, n):
        da = (dp[0] * a[0] + dp[1] * a[2] + dp[2] * a[1]) % m
        db = (dp[0] * a[1] + dp[1] * a[0] + dp[2] * a[2]) % m
        dc = (dp[0] * a[2] + dp[1] * a[1] + dp[2] * a[0]) % m
        dp = [da, db, dc]
    
    print(dp[0]) % m