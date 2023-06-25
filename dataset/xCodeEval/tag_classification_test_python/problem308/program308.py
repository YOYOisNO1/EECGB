    n,m,k = list(map(int,input().split()))
    
def st(n, x = 2):
        if n==1:
            return x
        if n==0:
            return 1
        s = st(n//2, x)
        return ((((s*s)%1000000007)* st(n%2,x))%1000000007)
    
    
    if k==1:
        ans = st(n-1, st(m-1))
        print(ans%1000000007)
        
    else:
        
        if (n+m)%2==0:
            ans = st(n - 1, st(m - 1))
            print(ans%1000000007)
        else:
            print(0)