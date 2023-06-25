    n, k, d = map(int, input().split())
    MOD = 1000000007
    dp = [[-1 for x in range(2)] for x in range(n + 10)]
    
    
def count_paths(s, f=0):
        if s == 0:
            if f == 0:
                return 0
            return 1
    
        if dp[s][f] != -1:
            return dp[s][f]
        res = 0
        for x in range(1, k + 1):
            if s - x >= 0:
                res += count_paths(s - x, f | (x >= d)) % MOD
        dp[s][f] = res
        return dp[s][f]
    
    print(count_paths(n)) % MOD
    