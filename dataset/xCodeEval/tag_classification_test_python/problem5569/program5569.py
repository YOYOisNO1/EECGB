def program5569():
    x,n=map(int,input().split())
    i=2
    a=[]
    while i*i<=x:
        if x%i==0:
            a.append(i)
            while x%i==0:
                x/=i
        i+=1
    if x!=1:
        a.append(x)
    
    ans=1
    mod=10**9+7
    for i in a:
        num=i
        cnt=0
        while num<=n:
            cnt+=(n/num)
            num*=i
        ans=(ans*pow(i,cnt,mod))%mod
    print(ans)