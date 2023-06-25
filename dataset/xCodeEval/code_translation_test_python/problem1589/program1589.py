def program1589():
    N, MOD = map(int, input().split())
    DP = [0] * N
    DP[0] = 1
    Cum = [0] * (N + 1)
    Cum[1] = 1
    for i1 in range(1, N):
        i2 = N - i1
        Value = Cum[i1]
        for j in range(2, N + 1):
            if i2 * j > N: break
            Value += Cum[N - i2 * j + 1] - Cum[max(0, N - i2 * j - j + 1)]
            Value %= MOD
        Cum[i1 + 1] += Cum[i1] + Value
        Cum[i1 + 1] %= MOD
        DP[i1] = Value
    print(DP[-1])