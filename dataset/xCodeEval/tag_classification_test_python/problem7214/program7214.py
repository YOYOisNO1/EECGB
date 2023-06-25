    n,k,l,m = map(int, input().split())
def mul(m1,m2):
        return  [(m1[0]*m2[0]+m1[1]*m2[2])%m, (m1[0]*m2[1]+m1[1]*m2[3])%m, (m1[2]*m2[0]+m1[3]*m2[2])%m, (m1[2]*m2[1]+m1[3]*m2[3])%m]
        
        
    M = [1,1,1,0]
def bpow(m1,n):
        if n == 1: return m1
        if (n%2) == 0:
            
            m1 = mul(m1,m1)
            return bpow(m1,n/2)
        else:
            return mul(m1,bpow(m1,n-1))
def fib(n):
        if n == 0 : return 0
        m = bpow([1,1,1,0],n)
        return m[2]
    
    if k >= 2**l:
        print(0)
        quit()
    
    ans = 1
    for i in range(l):
        c = (k >> i)&1
        if c == 0: ans *= fib(n+2)
        else: ans *= (pow(2,n,m) - fib(n+2))
        #print(c,) ans, fib(n), 2**n
    print(ans%m)