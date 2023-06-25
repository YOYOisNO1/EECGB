    MOD=998244353
def add(x,y):
        x+=y
        while x>=MOD:
            x-=MOD
        while x<0:
            x+=MOD
        return x
def multipication(x,y):
        return (x*y)%MOD
def binpow(x,y):
        z=1
        while y>0:
            if y%2==1:
                z=multipication(z,x)
            x=multipication(x,x)
            y=y//2
        return z
def inversion(x):
        return binpow(x,MOD-2)
def division(x,y):
        return multipication(x,inversion(y))
    n,k=list(map(int,input().split()))
    factorial=[1]
    for i in range(1,500001):
        factorial.append(multipication(i,factorial[-1]))
def combination(x,y):
        if y>x:
            return 0
        return division(factorial[x],multipication(factorial[y],factorial[x-y]))
    answer=0
    for i in range(1,n+1):
        d=n//i
        answer=add(ans,combination(d-1,k-1))
    print(answer)