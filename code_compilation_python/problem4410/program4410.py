def calc(n,m,k):
        if k == 1 or k > n:
            return (m**n)%(1e9+7)
        if k == n:
            if n % 2 == 1:
                return (m**((n+1)/2))%(1e9+7)
            else:
                return (m**((n)/2))%(1e9+7)
        if k % 2 == 1:
            return m**2
        return m
    
    n,m,k = map(int,input().split())
    
    print int(calc(n,m,k))