def program1985():
    import sys
    input = sys.stdin.readline
    I = lambda : list(map(int,input().split()))
    
    n,k,d=I()
    
    md=10**9+7
    dp=[[0,0] for i in range(102)]
    dp[0][0] = 1
    for i in range(1,n+1):
    	for j in range(1,k+1):
                if  i<j: 
                	break
                
                if(j < d):
                    dp[i][0]=(dp[i][0]+dp[i-j][0])%md
                    dp[i][1]=(dp[i][1]+dp[i-j][1])%md
                else:
                    dp[i][1]=(dp[i][1]+dp[i-j][0]+dp[i-j][1])%md
    
    print(dp[n][1])