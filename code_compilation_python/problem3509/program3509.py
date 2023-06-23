def program3509():
    import math
    
    
    if __name__ == '__main__':
        n, l, r = list(map(int, input().split()))
        mod_counts = [
            math.floor(r/3) - math.ceil(l/3) + 1, math.floor((r-1)/3) - math.ceil((l-1)/3) + 1,
            math.floor((r+1)/3) - math.ceil((l+1)/3) + 1]
        dp = [[None] * 3 for _ in range(n)]
        dp[0] = mod_counts
        for i in range(1, n):
            dp[i][0] = (dp[i-1][0] * mod_counts[0]) + (dp[i-1][1] * mod_counts[2]) + (dp[i-1][2] * mod_counts[1])
            dp[i][1] = (dp[i-1][0] * mod_counts[1]) + (dp[i-1][1] * mod_counts[0]) + (dp[i-1][2] * mod_counts[2])
            dp[i][2] = (dp[i-1][0] * mod_counts[2]) + (dp[i-1][1] * mod_counts[1]) + (dp[i-1][2] * mod_counts[0])
        res = dp[-1][0]
        print(res % (10 ** 9 + 7))