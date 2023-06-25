    INF = int(1e18)
    
def reverse(s):
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
        return s
    
    dp = []
    for i in range(61):
        dp += [[]]
        for j in range(61):
            dp[i] += [[]]
            for k in range(61):
                dp[i][j] += [INF]
    n = int(input())
    ff = input()
    k = []
    for i in range(len(ff)):
        k += ff[i]
    k = reverse(k)
    dp[0][0][0] = 0
    for kk in range(1, len(k) + 1):
        for i in range(1, len(k) + 1):
            s = ""
            for j in range(1, i + 1):
                s += k[i - j]
                if k[i - j] == '0':
                    if j == 1:
                        mn = INF
                        for jj in range(0, 61):
                            mn = min(mn, dp[i - j][jj][kk - 1])
                        if mn != INF:
                            dp[i][j][kk] = mn
                if s[0] == '0':
                    continue
                d = int(s)
                if d < n:
                    mn = INF
                    for jj in range(0, 61):
                        mn = min(mn, dp[i - j][jj][kk - 1])
                    if mn != INF:
                        dp[i][j][kk] = mn + pow(n, kk - 1) * d
    ans = INF
    n = len(k)
    for k in range(1, 61):
        for j in range(0, 61):
            ans = min(ans, dp[n][j][k])
    print(ans)