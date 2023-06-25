def program7171():
    import sys
    input = sys.stdin.readline
    MOD = 998244353
    N, K = map(int, input().split())
    N -= 1
    Kaijo = [1] * (N + 1)
    KaijoInv = [1] * (N + 1)
    for i in range(1, N + 1):
        Kaijo[i] = Kaijo[i - 1] * i % MOD
        KaijoInv[i] = pow(Kaijo[i], MOD - 2, MOD)
    nCr = lambda n, r: 0 if r > n else Kaijo[n] * KaijoInv[n - r] % MOD * KaijoInv[r] % MOD
    nPr = lambda n, r: 0 if r > n else Kaijo[n] * KaijoInv[n - r] % MOD
    
    DP = [[0] * (K + 1) for _ in range(N + 1)]
    DP[0][0] = 1
    for i in range(N + 1):
        for j in range(K):
            for k in range(N - i + 1):
                DP[i + k][j + 1] += nCr(i + k, k) * DP[i][j] % MOD * pow(K - j, (i + k - 1) * k - (k * (k - 1) // 2), MOD) % MOD
                DP[i + k][j + 1] %= MOD
    print(DP[N][K])