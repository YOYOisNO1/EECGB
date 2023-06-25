def program6548():
    # OEIS implementation
    
    MOD = 10 ** 9 + 7
    
    n = input()
    MAX = 2 * n + 10
    fact = [1] * MAX
    for i in xrange(1, MAX):
        fact[i] = fact[i - 1] * i
        if fact[i] >= MOD: fact[i] %= MOD
    
    invf = [1] * MAX
    invf[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
    for i in xrange(MAX - 2, -1, -1):
        invf[i] = invf[i + 1] * (i + 1)
        if invf[i] >= MOD: invf[i] %= MOD
    
    inv = [pow(i, MOD - 2, MOD) for i in xrange(MAX)]
    
    catalan = [(fact[2 * i] * invf[i] * invf[i] * inv[i + 1]) % MOD for i in xrange(n + 3)]
    
    a = [1]
    ans = 1
    for i in xrange(n):
        x = a[-1]
        y = (catalan[i + 3] - x) * (500000004)
        y %= MOD
        ans += y
        if ans >= MOD: ans -= MOD
        a.append(y)
    
    ans -= y
    print(ans) % MOD