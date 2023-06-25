def solve(n, k, d):
    
        dp = []
        modulo = 1000000007
        for i in range(n+1):
            dp.append([0]*(n+1))
    
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, k+1):
                if i-j < 0:
                    break
                if j < d:
                    dp[i][0] = (dp[i][0]+dp[i-j][0]) % modulo
                    dp[i][1] = (dp[i][1]+dp[i-j][1]) % modulo
                else:
                    dp[i][1] = (dp[i][1]+dp[i-j][0]) % modulo
                    dp[i][1] = (dp[i][1]+dp[i-j][1]) % modulo
        return dp[n][1]
    
    
def main():
        n, k, d = list(map(int, input().split()))
        print(solve(n, k, d))
    
    
    if __name__ == "__main__":
        main()