    # from math import factorial
    import re
    
    
def factorial(n):
        if n == 0:
            return 1
        else:
            for i in range(1, n):
                n = (n * i) % 1000000007
        return n
    
    
def exgcd(a, b, c):
        if b == 0:
            c[0] = 1
            c[1] = 0
            return a
        else:
            ret = exgcd(b, a % b, c)
            tmp = c[0] - a // b * c[1]
            c[0] = c[1]
            c[1] = tmp
            return ret
    
    
def inv(a, b):
        c = [0, 1]
        exgcd(a, b, c)
        return c[0] % b
    
    
def slove(n):
        f2n = factorial(2 * n - 1) % 1000000007
        fn = factorial(n) % 1000000007
        fn1 = factorial(n - 1) % 1000000007
        div = (fn * fn1) % 1000000007
        ninv = inv(div, 1000000007)
    
        ret = (2 * f2n * ninv - n) % 1000000007
        return ret
    
    
    n = int(input())
    print(slove(n))