    from math import sqrt
def F(n):
        if n <= 2:
            return 1
        if n % 2 == 0:
            k = F(n/2)
            return k*(2*F(n/2+1)-k)
        else:
            k = F(n/2+1)
            l = F(n/2)
            return k*k+l*l
        """
        n += 2
        print n
        return int(round(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))
        """
    
    
    n, k, l, m= map(int,input().split())
    
    ans = 1
    
    if k >= (1<<l):
        print 0
    else:
        zero = F(n+2) 
        one = (((1<<n) - F(n+2)))
        
        while l > 0:
            bit = k&1
            k = k >> 1
            l -= 1
    
            if bit == 0:
                ans *= zero
                ans %= m
                #print bit,zero,ans
            else:
                ans *= one
                ans %= m
               # print bit,one,ans
    
        print ans