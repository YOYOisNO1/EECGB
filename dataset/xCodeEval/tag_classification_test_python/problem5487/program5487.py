    # Enter your code here. Read input from STDIN. Print output to STDOUT
    MAX = 71
    C=[[0]*MAX for i in range(MAX)]
    dp=[[0]*MAX for i in range(MAX)]
    
    C[0][0]=1
    for i in range(1, MAX):
        C[i][0]=1
    for i in range(1, MAX):
        for j in range(1, i+1):
            C[i][j]=C[i-1][j]+C[i-1][j-1]
    
    
def catalan(n):
        return C[2*n][n]//(n+1)
    
def solve(n, h):
        if(n==0): return 0
        if(n<h): return 0
        if(h<=1): return catalan(n)
        if(dp[n][h]): return dp[n][h];
        ans=0
        for k in range(0, n): 
            if(dp[n-k-1][h-1]==0):
                dp[n-k-1][h-1]=solve(n-k-1, h-1)
            
            if(dp[k][h-1]==0):
                dp[k][h-1]=solve(k, h-1)
            
            ans+=dp[n-k-1][h-1]*( catalan(k)-dp[k][h-1]) + catalan(n-k-1)*dp[k][h-1]
            
        
        dp[n][h]=ans
        return ans
    
    n, h=map(int, input().split())
    ans=solve(n, h)
    print(ans)