def program7393():
    l=lambda:map(int,input().split())  
    n,m=l()
    g=[[0 for _ in range(n)] for _ in range(n)] 
    for _ in range(m):
        u,v=l()
        u,v=u-1,v-1
        g[u][v],g[v][u]=1,1
    d=[sum(v) for v in g]
    ans=[0]*n
    for i in range(n): 
        if d[i]==n-1:
            ans[i]=1
    for i in range(n):
        if ans[i]==0:
            for j in range(i+1,n):
                if g[i][j]==0:
                    ans[j]=2
    for i in range(n):
        for j in range(i+1,n):
            if g[i][j]==1 and abs(ans[i]-ans[j])>1 or \
                g[i][j]==0 and abs(ans[i]-ans[j])<2:
                print('No')
                exit()
    print('Yes')
    print('').join(map(str,[chr(x+ord('a')) for x in ans]))