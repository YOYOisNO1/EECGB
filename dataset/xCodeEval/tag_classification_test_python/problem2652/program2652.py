    import math
    from decimal import *
    getcontext().prec = 30
    a,b=map(int,input().split())
    ans=0
def fn():
        global a,b
        if a<b:
            a,b=b,a
        if (a-b)%b==0:
            x=(a-b)//b
            a-=a
            b-=b
            return x+1
        x=math.ceil((a-b)/b)
        a-=x*b
        return x
    while a*b:
        #print(a,b)
        ans+=fn()
    print(ans)