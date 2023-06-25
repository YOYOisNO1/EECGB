def cou(n,k):
        w=1
        for i in range(n-k+1,n+1):
            w*=i
        for i in range (1,k+1):
            w//=i
        return w
    
    n,k=map(int,input().split())
    ans=0
    for i in range(1,n+1):
        pp=1;
        i1=i;
        for j in range(2,i+1):
            sch=0;
            while(i1%j==0):
                    sch+=1
                    i1//=j
            if (sch):
                pp*=cou(sch+k-1,sch)
        ans+=pp
        ans%=1000000007
    print(ans)