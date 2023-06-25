    
def ncr(n, r, p):
        # initialize numerator
        # and denominator
        num = den = 1
        for i in range(r):
            num = (num * (n - i)) % p
            den = (den * (i + 1)) % p
        return (num * pow(den,
                          p - 2, p)) % p
    
    
    # p must be a prime
    # greater than n
    # n, r, p = 10, 2, 13
    # print("Value of nCr % p is",
    # 			ncr(n, r, p))
    
    n, m = map(int, input().split())
    p = 998244353
    
    ans = ncr(m, n - 1, p)
    
    ans = (ans * (n - 2) % p) % p
    for i in range(n - 3):
        ans = (ans * 2) % p
    print(ans)