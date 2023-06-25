    MOD = 1000000007
    
    
def binpow(a,p,m):
        if p == 0: 
            return 1
        elif p == 1:
            return a
        elif (p&1)>0:
            return (a*binpow(a,p-1,m)) % m
        else:
            t = binpow(a,p/2,m)
            return (t*t)%m
    
    
    x, n = map(int, input().split())
    
    primes = []
    xx = x
    i = 2
    while i*i <= xx:
        if xx % i == 0:
            primes.append(i)
            while xx%i == 0:
                xx = xx / i
        i += 1
    
    if xx > 1:
        primes.append(xx)
    
    # print(primes)
    
    res = 1
    for p in primes:
        div = p
        while n >= div:
            res = res * binpow(p, n/div, MOD)
            res = res % MOD
            div = div * p
    
    print(res)