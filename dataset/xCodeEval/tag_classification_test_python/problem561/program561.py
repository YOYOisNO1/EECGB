    import math
    
def nCr(n,r):
        f=math.factorial
        return f(n)/f(r)/f(n-r)
    
    
    n=int(input())
    ans=n*(n-1)*(n-2)*(n-3)*(n-4)*nCr(n,5)
    print(ans)