def power(x,y,mod):
        res = 1
        for i in xrange(0,y):
            res = (res * x) % mod
        return res
    
def calc(n,m,k):
        if k == 1 or k > n:
            return power(m,n,(1e9+7))
        if k == n:
            if n % 2 == 1:
                return power(m,((n+1)/2),(1e9+7))
            else:
                return power(m,((n)/2),(1e9+7))
        if k % 2 == 1:
            return m**2
        return m
    
    n,m,k = map(int,input().split())
    
    print(int(calc(n,m,k)))