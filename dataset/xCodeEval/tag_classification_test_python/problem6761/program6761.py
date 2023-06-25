    a, b, c = map(int, input().split())
    p = 998244353
    
def f(x,y):
        x, y = min(x, y), max(x, y)
        t = 1
        r = 0
        for i in xrange(x+1):
            r = (r + t) % p
            t = t * (x-i) * (y-i)*pow(i+1, p-2, p) % p
        return r
    
    print(f(a,b)) * f(b,c) * f(c, a) % p