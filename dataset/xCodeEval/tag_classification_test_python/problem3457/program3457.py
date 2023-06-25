def bin_pow(base, p):
        MOD = 1000000007
        base = int(base)
        p = int(p)
        if(p == 1):
            return base   
    
        if(p % 2 == 0):
            t = int(bin_pow(base, p // 2))
            return (t * t) % MOD
    
        else:
            return (bin_pow(base, p - 1) * base) % MOD
    
    
    values = input().split()
    n = int(values[0])
    m = int(values[1])
    
    print(bin_pow(bin_pow(2, m) - 1, n))