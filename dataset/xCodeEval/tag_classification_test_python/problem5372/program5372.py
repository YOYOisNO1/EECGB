def program5372():
    
    
    mod = 10**9 + 7
    
    t = int(input())
    for _ in range(t):
        n, k = [int(i) for i in input().split()]
        if n % 2 == 0:
            a = 1
            last = 1
            phi = (pow(2, n-1, mod)-1)
            mu = 1
            _mu = pow(2, n, mod)
            for i in range(k):
                a = (phi*last + mu) % mod
                last = a
                mu = (mu*_mu) % mod
            print(a)
    
        else:
    
            r = (pow(2, n-1, mod) + 1)
            print(pow(r, k, mod))