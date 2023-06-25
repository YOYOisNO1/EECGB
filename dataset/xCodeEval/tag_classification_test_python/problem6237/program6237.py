def program6237():
    MOD = 10**9 + 7
    n = int(input())
    m = pow(2, n, MOD)
    print((m*(m+1)/2)) % MOD