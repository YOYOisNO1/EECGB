    MOD=1000000007
def power(a,n):
        res=1
        while n>0:
            if n&1:res=res*a%MOD
            a=a*a%MOD
            n>>=1
        return res
    for _ in range(int(input())):
        n,k=map(int,input().split())
        if k==0:print(1);continue
        poww=power(2,n-1)
        if n%2:
            print(power(poww+1,k)%MOD)
        else:
            ans=poww;y=poww*2;poww-=1
            for i in range(1,k):
                ans=(ans*poww%MOD+y%MOD)%MOD
                y=2*y*(poww+1)%MOD
            print(ans)
        