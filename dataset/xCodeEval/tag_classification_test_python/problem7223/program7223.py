    from math import sqrt
    
def exp(base,expo,mod):
        if expo == 0:
            return 1
        if expo == 1:
            return base % mod
        if expo % 2 == 0:
            y = exp(base,expo/2,mod)
            return (y*y)% mod
        else:
            y = exp(base,expo/2,mod)
            return (y*y*base)% mod
    
    store = {1:1,2:1,3:2}
    
def fast(n,m):
        if n == 1:
            tmp = [[1,1],[1,0]]
            return tmp
        a = fast(n/2,m)
        b = [[0]*2 for _ in range(2)]
        b[0][0] = (a[0][0] * a[0][0] + a[0][1]*a[1][0]) % m
        b[1][0] = (a[0][0] * a[0][1] + a[0][1]*a[1][1]) % m
        b[0][1] = b[1][0]
        b[1][1] = (a[1][0] * a[0][1] + a[1][1]*a[1][1]) % m
        if n%2 == 0:
            return b
        c = [[0]*2 for _ in range(2)]
        c[0][0] = (b[0][0]+b[1][0])%m
        c[0][1] = c[1][0] = b[0][0]
        c[1][1] = b[0][1]
        return c
    
        
    """
def F(n):
        if n in store:
            return store[n]
        print(n)
        if n % 2 == 0:
            k = F(n/2)
            store[n] = k*(2*F(n/2+1)-k)
            return store[n]
        else:
            k = F(n/2+1)
            l = F(n/2)
            store[n] = k*k+l*l
            return store[n]
    
        #n += 2
        #print(n)
        #return int(round(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))))
    """
    
    
    n, k, l, m= map(int,input().split())
    
    ans = 1
    
    if k >= (1<<l):
        print(0)
    else:
        zero = fast(n+1,m)[0][0]
        one = (((exp(2,n,m)) - zero))%m
        #print("OK")
        
        while l > 0:
            bit = k&1
            k = k >> 1
            l -= 1
    
            if bit == 0:
                ans *= zero
                ans %= m
                #print(bit,zero,ans)
            else:
                ans *= one
                ans %= m
                #print(bit,one,ans)
            if k == 0:
                ans *= exp(zero,l,m)
                break
    
        print(ans%m)