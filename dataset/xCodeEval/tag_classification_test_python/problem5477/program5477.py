def program5477():
    n,h=map(int,input().split())
    
    L=[]
    for i in range(n+1):
        g=[]
        for j in range(n+1):
            g.append(0)
        L.append(g)
    L[0][0]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            sumu=0
            for m in range(1,i+1):
                t1=L[m-1][j-1]
                tot=0
                for k in range(0,j):
                    tot+=L[i-m][k]
                t1*=tot
    
                t2=L[i-m][j-1]
                tot=0
                for k in range(0,j-1):
                    tot+=L[m-1][k]
                t2*=tot
                sumu+=(t1+t2)
            L[i][j]=sumu
    
    ans=0
    for i in range(h,n+1):
        ans+=L[n][i]
    
    print(ans)
            
                    