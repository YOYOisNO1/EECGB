def program5415():
    import sys
    from math import gcd
    input = sys.stdin.readline
    mod = 10**9+7
    
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        w0 = 1
        pow_n_low = 1
        for _ in range(n-1):
            pow_n_low *= 2
            pow_n_low %= mod
        pow_n = (pow_n_low * 2) % mod
        ans = w0
        pow_n_k_low = 1
        for i in range(1, k+1):
            if n % 2 == 0:
                ans = ans*(pow_n_low-1) + pow_n_k_low
                ans %= mod
                pow_n_k_low *= pow_n
                pow_n_k_low %= mod
            if n % 2 == 1:
                ans = ans * (pow_n_low + 1)
                ans %= mod
        print(ans)
    
    
    
    
    
    
    