    n, k, l, BASE = map(int,input().split())
    d = {0:1, 1:1, 2:(2 % BASE)}
    
def power(n):
        if n == 0: return 1
        if n & 1 > 0:
            return (power(n-1) << 1) % BASE
        u = power(n >> 1) % BASE
        return u * u % BASE
    
def fib(n):
        if d.get(n) != None:
            return d[n]
        if n & 1 < 1:
            d[n] = (fib((n >> 1) - 1)*fib((n >> 1) - 1)+fib(n >> 1)*fib(n >> 1))%BASE
        else:
            d[n] = (fib((n >> 1) )*fib((n >> 1) + 1)+fib((n >> 1) - 1)*fib(n >> 1))%BASE
        return d[n]
    
    u = fib(n+1)
    v = (power(n) + BASE - u) % BASE
    a = 1
    for i in range(l):
        if k & 1 == 0:
            a *= u
        else:
            a *= v
        a %= BASE
        k >>= 1
    if k > 0:
        a = 0
    
    print(a % BASE)
            