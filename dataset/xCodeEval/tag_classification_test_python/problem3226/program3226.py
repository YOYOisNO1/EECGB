def program3226():
    import sys
    
    k = int(input())
    t = input()
    
    n = len(t)
    
    inf = 10**18 + 1
    
    dp = [inf] * (n + 1)
    for i in range(n + 1):
        dp[i] = [inf] * (n + 1)
    
    t = t[::-1]
    dp[0][0] = 0
    for i in range(n + 1):
        for j in range(n + 1):
            if dp[i][j] == inf:
                continue
            cur = 0
            for len in range(0, n):
                if i + len >= n:
                    break
                symb = ord(t[i + len]) - ord('0')
                if symb == 0 and len > 0:
                    continue
                cur = cur + symb * 10**len
                if cur >= k:
                    break
                neww = dp[i][j] + cur * k**j
                dp[i + len + 1][j + 1] = min(dp[i + len + 1][j + 1], neww)
    
    ans = -1
    for i in range(1, n + 1):
        if ans == -1 or ans > dp[n][i]:
            ans = dp[n][i]
    
    print(ans)