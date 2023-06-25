def program7672():
    S, T = input(), input()
    s1 = [1 if c=='(' else -1 for c in S]
    s2 = [1 if c=='(' else -1 for c in T]
    len1, len2 = len(s1), len(s2)
    
    inf = 10**9
    dp = [[[inf]*(len1+len2+1) for _ in range(len2+1)] for _ in range(len1+1)]
    dp[0][0][0] = 0
    
    for i in range(len1+1):
        for j in range(len2+1):
            for k in range(len1+len2):
                if i < len1:
                    k1 = k + s1[i]
                    if k1 < 0:
                        dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k]+2)
                    else:
                        dp[i+1][j][k1] = min(dp[i+1][j][k1], dp[i][j][k]+1)
    
                if j < len2:
                    k2 = k + s2[j]
                    if k2 < 0:
                        dp[i][j+1][k] = min(dp[i][j+1][k], dp[i][j][k]+2)
                    else:
                        dp[i][j+1][k2] = min(dp[i][j+1][k2], dp[i][j][k]+1)
    
                if i < len1 and j < len2:
                    if s1[i] == s2[j]:
                        if k1 < 0:
                            dp[i+1][j+1][k] = min(dp[i+1][j+1][k], dp[i][j][k]+2)
                        else:
                            dp[i+1][j+1][k1] = min(dp[i+1][j+1][k1], dp[i][j][k] + 1)
    
    k = 0
    length = inf
    for i in range(len1+len2+1):
        if dp[len1][len2][i] + i < length:
            length = dp[len1][len2][i] + 1
            k = i
    
    i, j = len1, len2
    ans = [')']*k
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
            if dp[i-1][j-1][k-s1[i-1]] + 1 == dp[i][j][k]:
                ans.append(S[i-1])
                k -= s1[i-1]
                i -= 1
                j -= 1
                continue
            elif k == 0 and s1[i-1] == -1 and dp[i-1][j-1][k] + 2 == dp[i][j][k]:
                ans.extend((S[i-1], '('))
                i -= 1
                j -= 1
                continue
        if i > 0:
            if dp[i-1][j][k-s1[i-1]] + 1 == dp[i][j][k]:
                ans.append(S[i-1])
                k -= s1[i-1]
                i -= 1
                continue
            elif k == 0 and s1[i-1] == -1 and dp[i-1][j][k] + 2 == dp[i][j][k]:
                ans.extend((S[i-1], '('))
                i -= 1
                continue
        if j > 0:
            if dp[i][j-1][k-s2[j-1]] + 1 == dp[i][j][k]:
                ans.append(T[j-1])
                k -= s2[j-1]
                j -= 1
                continue
            elif k == 0 and s2[j-1] == -1 and dp[i][j-1][k] + 2 == dp[i][j][k]:
                ans.extend((T[j-1], '('))
                j -= 1
                continue
    
        raise Exception(i, j, k, S[i-1], T[j-1])
    
    print(*ans[::-1], sep='')