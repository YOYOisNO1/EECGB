def program6029():
    n,m=map(long, input().split())
    ans=long(1)
    mult=long(3)
    while n:
        if n&1!=0:
            ans=(ans*mult)%m;
        mult=(mult**2)%m
        n/=2
    if ans!=0:
        print(long(ans-1))
    else:
        print(m-1) 