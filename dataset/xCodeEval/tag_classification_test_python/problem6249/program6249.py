    import math
    MOD=1000000007
    # assume first is 2
def power(b):
        if (b==0):
            return 1
        if (b==1):
            return 2
        if (b==2):
            return 4
        if (b%2==0):
            x=power(b/2)
            return (x*x)%MOD
        else:
            x=power((b-1)/2)
            ll=(x*x)%MOD
            return (2*ll)%MOD
    n=int(input(""))
    if (n==0):
        print(1)    
    else:
        ans=power(n-1)*3
        ans+=power(2*n-1)
        ans-=power(n)
        print(ans%MOD)