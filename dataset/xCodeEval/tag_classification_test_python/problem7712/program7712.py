    MOD = 1000000007
    n = input() + 1
    
def modfactorial(x, mod=MOD):
        ans = 1
        for i in xrange(x):
            ans = ans * (i+1) % mod
        return ans
    
def gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = gcd(b % a, a)
            return (g, x - (b / a) * y, y)
    
def modinverse(a, mod=MOD):
        g, x, y = gcd(a, mod)
        return x % mod
    
    print((modfactorial(n*2)*modinverse((modfactorial(n)**2))-1)) % 1000000007
    