def gh(a,b):
        t=1
        while b>0:
            if b&1:t=(t*a)%1000000007
            b=b>>1
            a=(a*a)%1000000007
        return t
    a=int(input())
    if a==0:print(1);exit()
    print((((gh(2,2*a-1)+gh(2,a-1))%1000000007)))