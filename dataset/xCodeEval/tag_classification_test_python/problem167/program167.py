def program167():
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    rem_parity = [0, 0]
    for i in range(1, n+1):
        if i not in s:
            rem_parity[i % 2] += 1
    
    inf = 10**9
    dp = [[[inf]*2 for _ in range(n)] for _ in range(n)]
    rem = rem_parity[0] + rem_parity[1]
    
    if a[0] != 0:
        dp[0][rem_parity[0]][a[0] % 2] = 0
    else:
        if rem_parity[0] > 0:
            dp[0][rem_parity[0]-1][0] = 0
        if rem_parity[1] > 0:
            dp[0][rem_parity[0]][1] = 0
        rem -= 1
    
    for i, x in enumerate(a[1:]):
        if x > 0:
            par = x % 2
            for j in range(n):
                for k in range(2):
                    dp[i+1][j][par] = min(dp[i+1][j][par], dp[i][j][k] + ((k + par) % 2))
    
        else:
            rem -= 1
            for j in range(n):
                for k in range(2):
                    if j > 0:
                        dp[i+1][j-1][0] = min(
                            dp[i+1][j-1][0],
                            dp[i][j][k] + (0 if k == 0 else 1)
                        )
                    if j <= rem:
                        dp[i+1][j][1] = min(
                            dp[i+1][j][1],
                            dp[i][j][k] + (0 if k == 1 else 1)
                        )
    
        # print(f'i={i}, x={x}, rem={rem}, {dp[i+1]}')
    
    print(min(dp[-1][0]))