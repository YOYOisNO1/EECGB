    from math import *
    
    MOD = 1000000007
    
def f(n, b):
        if n == 1:
            return b
        else:
            if n % 2 == 0:
                a = f(n/2, b) ** 2
                return a % MOD
            else:
                return (b * f((n-1)/2, b) ** 2) % MOD
     
    t = int(input())
    k = 250000002
    if t % 2 == 0:
        print((k) * (f(t, 3) + 3)) % MOD
    else:
        print((k) * (f(t, 3) - 3)) % MOD