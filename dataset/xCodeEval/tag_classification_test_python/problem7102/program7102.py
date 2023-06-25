    __author__ = 'heckboy'
    #!/usr/bin/env python
def getinput():
        return map(int, input().split())
def opow(a, b, mod):
        ans = 1
        while b > 0:
            if b % 2 == 1:
                ans *= a
                ans %= mod
            a *= a
            a %= mod
            b /= 2
        return ans
    
    p, k = getinput()
    mod = 1000000007
    ans = 0
    if k == 0:
        ans = opow(p, p - 1, mod)
    else:
        for i in xrange(1, p):
            if (p - 1) % i == 0 and opow(k, i, p) == 1:
                ans = opow(p, (p - 1) / i, mod)
                if k == 1:
                    ans *= p
                    ans %= mod
                break
    print(ans)