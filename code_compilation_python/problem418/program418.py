    n = int(input())
    MOD = 998244353
    
    
def fib(n):
        f = [0, 0, 1, 2, 3]
    
        for i in range(5, n+1):
            f.append((f[i-1] + f[i-2]) % MOD)
        return f[n]
    
    
    x = fib(n)
    y = pow(2, n, MOD)
    print((x*pow(y, MOD-2, MOD)) % MOD)