    from math import sqrt,ceil
def prime(n):
        c=n
        l=[]
        i=3
        if n%2==0:
            l.append(2)
        while n%2==0:
            n=n//2
        while i<=ceil(sqrt(c)):
            if n%i==0:
                l.append(i)
            while n%i==0:
                n=n//i
            i+=2
        if n!=1:
            l.append(n)
        
        return(l)
    mod=10**9+7
    x,n=map(int,input().split())
    f=prime(x)
    ans=1
    for p in f:
        k=p
        while k<=n:
            
            ans*=pow(p,n//k,mod)
            ans=ans%mod
            k*=p
    print(ans)