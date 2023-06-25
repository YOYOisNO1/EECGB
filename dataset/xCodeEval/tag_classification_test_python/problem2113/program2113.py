    n, k, d = [int(i) for i in input().split()]
    
    
    mod = 1e9+7
    dp = [[-1 for i in range(2)] for j in range(n+1)]
    
def dfs(cur_sum: int, chk: bool):
        if cur_sum == n and chk==True:
            return 1
    
        if cur_sum == n and chk==False:
            return 0
        
        if cur_sum > n:
            return 0
    
        if (dp[cur_sum][chk] != -1):
            return dp[cur_sum][chk]
    
        ans = 0
        for i in range(1, k+1):
            if i < d:
                ans += dfs(cur_sum + i, chk)
            else:
                ans += dfs(cur_sum + i, True)
        dp[cur_sum][chk] = ans % mod
        return ans % mod
    
    ans = int(dfs(0, False))
    print(ans)