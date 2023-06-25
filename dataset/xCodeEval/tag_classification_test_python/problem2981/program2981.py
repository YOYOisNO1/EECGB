    MOD=998244353
def power(x, a):
        if(a==0):
            return(1)
        z=power(x, a//2)
        z=(z*z)%MOD
        if(a%2):
            z=(z*x)%MOD
        return(z)
def fact(n):
        factn=1
        for i in range(2, n+1):
            factn=(factn*i)%MOD
        return(factn)
def ncr(n, r):
        return((fact(n)*power(fact(r), MOD-2)*power(fact(n-r), MOD-2))%MOD)    
    [n, m, k]=list(map(int, input().split()))
    print((ncr(n-1, k)*m*power(m-1, k))%MOD)