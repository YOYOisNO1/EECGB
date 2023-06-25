def program2133():
    x=map(int,input().split(' '))
    path=x[0]
    tree=x[1]
    d=x[2]
    dp=[[0 for x in range(2)] for x in range(200)]
    dp[0][1]=1
    dp[0][0]=1
    for i in range(1,path+1):
        for j in range(1,min(tree,d-1)+1):
            if i<j:
                break
            dp[i][0]+=dp[i-j][0]
    
    
    for i in range(1,path+1):
        for j in range(1,tree+1):
            if i<j:
                break
            dp[i][1]+=dp[i-j][1]
    ans = dp[path][1]-dp[path][0]
    ans%=(1000000007)
    print(ans)