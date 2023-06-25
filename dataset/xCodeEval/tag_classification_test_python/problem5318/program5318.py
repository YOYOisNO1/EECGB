    from sys import stdin
    input = stdin.readline
    
def add(x , y):return ((x%mod) + (y%mod))%mod
def sub(x , y):return (x - y + mod)%mod
    
    
def answer():
    
        dp = [0]*(n + 1)
        prefix = [0]*(n + 2)
    
        dp[n] = 1
    
        for i in range(n , 0 , -1):
    
            dp[i] = add(dp[i] , prefix[i + 1])
    
            j = 2
            while(i*j <= n):
    
                dp[i] = add(dp[i] , prefix[i*j])
                if((j*i + j) <= n):dp[i] = sub(dp[i] , prefix[j*i + j])
                j += 1
    
                
            prefix[i] = add(prefix[i + 1] , dp[i])
    
        return dp[1]
    
        
        
    
    for T in range(1):
    
        n , mod = map(int,input().split())
    
        print(answer())