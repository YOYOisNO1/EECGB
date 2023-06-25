def program3013():
    n=int(input())
    mod=10**6+3
    if(n==0):
        print(1)
    
    elif(n==1):
        print(1)
    
    elif(n==2):
        print(3)
    
    else:
        nn=n
        ans=pow(2,2*n-1,mod)+pow(2,n-1,mod)
        n-=1
        ans+=pow(2,2*n-1,mod)+pow(2,n-1,mod)
        ans%=mod
        n-=1
        f=3
        while(n>=1):
            ans+=f*(pow(2,2*n-1,mod)+pow(2,n-1,mod))
            ans%=mod
            f*=3
            f%=mod
            n-=1
        ans=pow(2,2*nn,mod)-ans
        if(ans<0):
            ans+=mod
        print(ans)
            