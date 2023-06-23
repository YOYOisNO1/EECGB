    mod=1000000007
def fact(n):
        if(n==0):
            return 1
        else:
            return n*fact(n-1)%mod
def myPow(n,p):
        if(p==0):
            return 1
        res=myPow(n,p/2)
        res=res*res%mod
        if(p%2==1):
            res=res*n%mod
        return res
def rev(n):
        return myPow(n,mod-2)
def comb(n,k):
        if(k>n):
            return 0
        res=fact(n)
        res*=rev(fact(k)*fact(n-k)%mod)
        res%=mod    
        return res
    n,m,k=map(int,input().split())
    n-=1
    m-=1
    res=comb(n,2*k)*comb(m,2*k)%mod
    print res
    
        