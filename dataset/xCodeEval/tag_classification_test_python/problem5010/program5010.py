def program5010():
    w, b = map(int, input().split())
    dp = [[[1, 0] if i and not j else [0, 0] for j in range(b + 2)] for i in range(w + 2)]
    for i in range(1, w + 1):
        for j in range(1, b + 1):
            dp[i][j][0] = (i + j * (dp[i][j - 1][1])) / (i + j)
            dp[i][j][1] = j * ((j - 1) * dp[i][j - 2][0] + i * dp[i - 1][j - 1][0]) / (i + j) / (i + j - 1)
    print(dp[w][b][0])