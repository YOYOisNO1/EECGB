    MOD = 1000000007
    
    p,k  = tuple(int(i) for i in input().split(" "))
    
def powm(n, k):
        r = 1
        while k:
            r = (r * n) % MOD
            k -= 1
        return r
    
    if k == 0:
        print(powm(p,) p-1)
        exit(0)
    
    if k == 1:
        print(powm(p,) p)
        exit(0)
    
    m = 1
    x = k
    while x != 1:
        x = (x * k) % p
        m += 1
    
    print(powm(p,) (p - 1)/m)