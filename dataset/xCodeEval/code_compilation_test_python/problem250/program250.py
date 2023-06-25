def pow_fast_mod(a, b, div):
        s = 1
        while b > 0:
            if b % 2:
                s %= div
                a %= div
                s *= a
            a %= div
            a *= a
            b = (b // 2)
        return s % div
    
    [n, m, L, R] = [int(s) for s in input().split()]
    h = R-L
    mod = 998244353
    ret = 0
    if n%2 and m%2:
        ret = pow_fast_mod(h+1, n*m, mod)
    else:
        x = (h+1)**(n*m/2)
        a = x // 2
        a %= mod
        b = (x+1) // 2
        b %= mod
        ret = a*a+b*b
    
    print(int(ret%mod))