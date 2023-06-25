    from  decimal import *
    
def C(n,m):
        if m>n : return 0
        if m==0 or m==n : return 1
        if m>n-m : m=n-m
        ret = 1
        i,j = n,1
        while j<=m :
            ret = ret*i/j
            i=i-1
            j=j+1
        return ret
    
    n,m = map(int,input().split())
    ans = C(m,1)*C(n*m-1,n-1)
    if n>1 : ans += 2*C(m,2)*C(n*m-2,n-2)
    ans = Decimal(1.0/n) * Decimal(ans) / Decimal(C(n*m,n))
    print('%.16f') %ans