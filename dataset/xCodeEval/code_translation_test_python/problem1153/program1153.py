def program1153():
    n,d = map(int, input().split())
    s = input()
    dp = [n+1 for i in range(n+1)]
    if s[0] == 0 or s[n-1] == 0:
        print("-1")
    else:
        dp[0] = 0
        for i in range(1, d+1):
            if s[i] == '1':
                dp[i] = 1
            else:
                dp[i] = -1
        for i in range(d+1, n):
            if s[i] == '1':
                for j in range(i-1, i-(d+1), -1):
                    if s[j] == '1' and dp[j] != -1:
                        dp[i] = min(dp[i], 1+dp[j])
                if dp[i] >= n:
                    dp[i] = -1
            else:
                dp[i] = -1
        print(dp[n-1])