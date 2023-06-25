    # 106C
    
def do():
        n, m, c0, d0 = map(int, input().split(" "))
        dp = [0] * (n + 1)
        for i in range(c0, n + 1):
            dp[i] = i // c0 * d0
        for _ in range(m):
            a, b, c, d = map(int, input().split(" "))
            for i in range(n, c - 1, -1):
                for j in range(1, a // b + 1):
                    if i >= j * c:
                        dp[i] = max(dp[i], dp[i - j * c] + j * d)
        return dp[-1]
    
    print(do())