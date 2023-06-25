def main():
    def rec(n, h):
            if sht[n][h]:
                return dp[n][h]
            
            sht[n][h] = 1
            
            if n == 0:
                dp[n][h] = h == 0
                return dp[n][h]
            
            if h == 0:
                return dp[n][h]
            
            if n < h:
                return dp[n][h]
            
            for i in range(n):
                for j in range(h):
                    dp[n][h] += rec(n - 1 - i, h - 1) * rec(i, j) + rec(n - 1 - i, j) * rec(i, h - 1)
                dp[n][h] -= rec(n - 1 - i, h - 1) * rec(i, h - 1)
                
            return dp[n][h]
            
        dp = [[0] * 40 for _ in range(40)]
        sht = [[0] * 40 for _ in range(40)]
        n, h = map(int, input().split())
        print(sum([rec(n, j) for j in range(h, n + 1)]))
        return 0
    
    main()