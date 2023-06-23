    from fractions import gcd
    
    N = input()
    H = dict()
    
def number (n,b):
        if not H.has_key((n,b)):
            if n == 1 and b == 1:       H[n,b] = 0
            elif n>b and b>0:           H[n,b] = (n-1)/b + number ((n-1)%b+1,b)
            elif b>n and n>0:           H[n,b] = (b-1)/n + number (n,(b-1)%n+1)
            else:                       H[n,b] = 10000000
        return H[n,b]
    
    m = min (number(N,b) for b in range (N+1))
    print m
    #print [b for b in range (N+1) if number(N,b)==m]
    # for b in range (N+1): print number(N,b),b,gcd(N,b)
    