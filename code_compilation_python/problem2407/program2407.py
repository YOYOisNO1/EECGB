    import sys
    input = sys.stdin.buffer.readline
    sys.setrecursionlimit(10**8) 
    n, k = [int(i) for i in input().split()]
    dp = [[-1]*(2005) for i in range(2005)]
    MOD=10**9+7
def solve(x,k):
        if(k==0):
            return 1
        elif(dp[x][k]!=-1):
            return dp[x][k]
        ans=0
        for i in range(x,n+1,x):
            ans+=solve(i,k-1)
        dp[x][k]=ans%MOD
        return dp[x][k]
    res=solve(1,k)
    print(res)
    
    
    
    
    
    
    
    
    
        
    
        
    
    
        
    
                        
    
    
    
    
        
    
        
    
    
        
    
                        
    
    
        
    
    
        
    
                        
    
    
    
    
        
    
                        
    