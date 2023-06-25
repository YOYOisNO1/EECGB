    n,k,l,m = map(int, input().split())
def mul(m1,m2):
        return [m1[0]*m2[0]+m1[1]*m2[2], m1[0]*m2[1]+m1[1]*m2[3], m1[2]*m2[0]+m1[3]*m2[2], m1[2]*m2[1]+m1[3]*m2[3]]
    
def fib(n):
        if n == 0 : return 0
        m = [1,1,1,0]
        m1 = [1,1,1,0]
        for i in range(n-1):
            m = mul(m,m1)
        return m[2]
    
    if k > 2**l:
        print 0
        quit()
    
    ans = 1
    for i in range(l):
        c = (k >> i)&1
        if c == 0: ans *= fib(n+2)
        else: ans *= (2**n - fib(n+2))
        #print c, ans, fib(n), 2**n
    print ans%m