    n, m = [int(x) for x in input().split()]
    
def eachn(n, m):
    def gcd(a, b):
            if b >= a:
                for t in range(a, 0, -1):
                    if b%t == 0 and a%t == 0:
                        return t
            else:
                return gcd(b,a)
        
    def f(n):
            dick = {0:1}
            for t in range(1,n+1):
                dick[t] = t//(gcd(dick[t-1], t))*dick[t-1]
            return dick
            
        g = f(n)
        
        num = 1
        for t in range(1,n+1):
            num = (((m // g[t]) % 998244353) * num) % 998244353
        
        em = m % 998244353
        numnot = 1
        for t in range(1,n+1):
            numnot = (em * numnot) % 998244353
        
        if numnot-num>=0:
            return numnot-num)
        else:
            return 998244353+numnot-num
    
    sum = 0    
    for i in range(1, n+1):
        sum += eachn(i, m)
    return sum