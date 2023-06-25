def program4177():
    phi = [0 for i in range(10 ** 6 + 1)]
    for i in range(1, 10**6+1):
        for j in range(2 * i, 10 ** 6 + 1, i):
            phi[j] += 1
    mod = 998244353
    n = int(input())
    if n == 1:
        print(1)
        exit()
    n = 2 * n
    dp = [0 for i in range(n + 1)]
    dp[2] = 1
    dp[4] = 3
    s = 4
    for i in range(6, n + 1, 2):
        dp[i] = (s + (phi[i // 2] + 1)) % mod
        s = (s + dp[i]) % mod
    print(dp[n])