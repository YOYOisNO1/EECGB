def program1289():
    a,b,n,x=map(int,input().split())
    mod=1000*1000*1000 +7
    sum=0
    if(a==1):
        sum=(x%mod+n*b%mod)%mod
    else:
        sum=(pow(a,n,mod)*x+(((b*(pow(a,n,mod)-1))%mod)*pow(a-1,mod-2,mod))%mod)%mod
        
    print(sum)