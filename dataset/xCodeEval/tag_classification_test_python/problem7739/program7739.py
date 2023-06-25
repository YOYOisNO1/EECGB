def program7739():
    dp=[]
    for i in xrange(333):
        tmp = []
        for j in xrange(333):
            tmp.append(0)
        dp.append(tmp)
    
    n = map(int,input().split())[0]
    a = map(int,input().split())
    s1="BitLGM"
    s2="BitAryo"
    
    if n==2:
        dp[0][0]=0
        for i in xrange(302):
            for j in xrange(302):
                if(dp[i][j]==0):
                    k=1
                    while i+k<=300:
                        dp[i+k][j]=1
                        k=k+1
                    k=1
                    while j+k<=300:
                        dp[i][j+k]=1
                        k=k+1
                    k=1
                    while i+k<=300 and j+k<=300:
                        dp[i+k][j+k]=1
                        k=k+1
        if dp[a[0]][a[1]]==1:
            print(s1)
        else: print(s2)
        exit(0)
    
    t = 0
    if n==1: t = a[0]
    else:
        t = (a[0]^a[1]^a[2])
    
    if(t>0):
        print(s1)
    else:
        print(s2)