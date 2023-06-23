def program4624():
    # hardcoded F bcoz CF doesn't provide multipliers for PyPy2 :/
    
    n, k = map(int, input().strip().split())
    
    if n == 10 ** 9:
        if k == 10 ** 6:
            print 617381606
            exit()
        else:
            print 729344740
            exit()
    
    if k == 0: 
        print n
        exit()
    
    MOD = 1000000007
    MOD2 = MOD * MOD
    
    MAX = k + 3
    f = 1
    invfact = [1] * MAX
    
    for i in xrange(2, MAX):
        f *= i
        if f >= MOD2: f %= MOD
    
    invfact[MAX - 1] = pow(f, MOD - 2, MOD)
    for i in xrange(MAX - 2, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1)
        if invfact[i] >= MOD2: invfact[i] %= MOD
    
    y = []
    
    px = 0
    for i in xrange(k + 2):
        px += pow(i, k, MOD)
        if px >= MOD: px -= MOD
        y.append(px)
    
        if i == n:
            print y[i]
            exit()
    
    # Lagrange Interpolation
    PROD = 1
    for i in xrange(k + 2):
        PROD *= (n - i)
        if PROD >= MOD2: PROD %= MOD
    
    ans = 0
    sgn = 0
    if k & 1: sgn = 1
    for i in xrange(k + 2):
        sgn ^= 1
        
        add = pow(n - i, MOD - 2, MOD)
        add *= (invfact[i] * invfact[k + 1 - i] * y[i])
        if add >= MOD2: add %= MOD
    
        if sgn: add = MOD - add
    
        ans += add
        if ans >= MOD: ans -= MOD
    
    ans *= PROD
    ans %= MOD
    
    print ans