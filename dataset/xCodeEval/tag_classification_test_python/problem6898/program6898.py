    INF=100000000007
    
def dist(a,b):
        d=(abs(a[0]-b[0])**2)+(abs(a[1]-b[1])**2)
        return d
    
    x0,y0=[int(x) for x in input().split()]
    L=[(x0,y0)]
    dis=[]
    n=int(input())
    for i in range(n):
        x,y=[int(x) for x in input().split()]
        L.append((x,y))
    
    for i in range(0,len(L)):
        h=[]
        for j in range(0,len(L)):
            d=dist(L[i],L[j])
            h.append(d)
        dis.append(h)
    
    dp=[INF]*((1<<n)+5)
    pre=[0]*((1<<n)+5)
    dp[0]=0
    
    for i in range(0,(1<<n)):
        if(dp[i]<INF):
            for j in range(0,n):
                if(i&(1<<j)==0):
                    for k in range(j,n):
                        if(i&(1<<k)==0):
                            ds=dis[j+1][k+1]+dis[0][j+1]+dis[k+1][0]
                            nw=(1<<j)|(1<<k)
                            if(ds+dp[i]<dp[i|nw]):
                                dp[i|nw]=min(dp[i|nw],ds+dp[i])
                                pre[i+nw]=i
    
                    break
    
    print(dp[(1<<n)-1])
    now=(1<<n)-1
    while(now!=0):
        print(0,) 
        tt=now^pre[now]
        for i in range(0,n):
            if(tt&(1<<i)):
                print(i+1,) 
        now=pre[now]
    
    print(0)               
            
        