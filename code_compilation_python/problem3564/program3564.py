def program3564():
    l=[0 for i in range(6)]
    r=[0 for i in range(6)]
    n=input()
    dp=[[0.0 for i in range(35)] for j in range(0.0)]
    cul=[[0.0 for i in range(35)] for j in range(0.0)]
        #For(i,0,n) cin>>l[i]>>r[i];
    for i in range(n):
        l[i]=input()
        r[i]=input()
        #For(i,0,n) For(j,l[i],r[i]+1) {dp[1<<i][j]=1.0/(r[i]+1-l[i]);}
    for i in range(n):
        for j in range(l[i],r[i]+1):
            dp[1<<i][j]=1.0/(r[i]+1-l[i])
    
        #For(i,0,n) For(j,1,10011) cul[1<<i][j]=dp[1<<i][j]+cul[1<<i][j-1];
    for i in range(n):
        for j in range(1,10011):
            cul[1<<i][j]=dp[1<<i][j]+cul[1<<i][j-1]
            
        #For(i,2,1<<n) For(j,1,1<<n) if((i|j)==i)
        #{
        #    int jj=i^j;
        #    if(jj==0) continue;
        #    //if(i==2) cout<<j<<' '<<(i|j)<<endl;
        #    For(k,1,10011)
        #    {
        #        dp[i][k]=dp[j][k]*cul[jj][k]+dp[jj][k]*cul[j][k-1];
        #        cul[i][k]=cul[i][k-1]+dp[i][k];
        #    }
        #}
    for i in range(2,1<<n):
        for j in range(1,1<<n):
            if((i|j)==i):
                jj=i^j
                if(jj==0):
                    continue
                for k in range(1,10011):
                    dp[i][k]=dp[j][k]*cul[jj][k]+dp[jj][k]*cul[j][k-1]
                    cul[i][k]=cul[i][k-1]+dp[i][k]
        #double ans=0.0;
    ans=0.0
        #For(i,0,n)
        #{
        #    int k=(1<<i)^((1<<(n))-1);
        #    cur=0.0;
        #    For(j,1,10011)
        #    {
        #        cur+=(j-1)*dp[k][j-1];
        #        ans+=cur*dp[1<<i][j];
        #        //if(j==6) cout<<cur<<endl;
        #        //if(cur*dp[1<<i][j]) cout<<k<<' '<<i<<' '<<j<<' '<<cur*dp[1<<i][j]<<endl;
        #    }
        #    //cout<<ans<<endl;
        #}
    for i in range(n):
        k=(1<<i)^((1<<n)-1)
        cur=0.0
        for j in range(10011):
            cur+=(j-1)*dp[k][j-1]
            ans+=cur*dp[1<<i][j]
        #For(i,1,10011) For(j,1,(1<<n)-1)
        #{
        #    int b=0;
        #    For(jj,0,n) if(j&(1<<jj)) b++;
        #    if(b>=2)
        #    {
        #        cur=1.0*i;
        #        int k=j^((1<<(n))-1);
        #        cur*=cul[k][i-1];
        #        For(jj,0,n) if((1<<jj)&j) cur*=dp[1<<jj][i];
        #        ans+=cur;
        #    }
        #}
    for i in range(10011):
        for j in range(1,(1<<n)-1):
            b=0
            for jj in range(n):
                if(j&(1<<jj)):
                    b+=1
            if b>=2:
                cur=1.0*i
                k=j^((1<<n)-1)
                cur*=cul[k][i-1]
                for jj in range(n):
                    if (1<<jj)&j:
                        cur*=dp[1<<jj][i]
                ans+=cur
        #For(i,1,10011)
        #{
        #    cur=1.0*i;
        #    For(j,0,n) cur*=dp[1<<j][i];
        #    ans+=cur;
        #}
    for i in range(10011):
        cur=1.0*i
        for j in range(n):
            cur*=dp[1<<j][i]
        ans+=cur
    print ans