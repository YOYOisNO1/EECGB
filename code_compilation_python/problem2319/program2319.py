    from math import sqrt
def F(n):
        n += 2
        return int(round(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))
    
    
    n, k, l, m= map(int,input().split())
    
    ans = 1
    
    if k >= (2<<l):
        print 0
    else:
        while l > 0:
            bit = k&1
            k = k >> 1
            l -= 1
    
            if bit == 0:
                ans *= F(n)
                ans %= m
            else:
                ans *= ((1<<n) - F(n))
                ans %= m
                
            #print bit,F(n),ans
    
        print ans