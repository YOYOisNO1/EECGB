def program4699():
    R = lambda: map(int, input().split())
    arr = list(map(int, input()))
    n = len(arr)
    dp = [[0] * 10 for i in range(n)]
    for i in range(10):
        dp[n - 1][i] = 1
    for i in range(n - 2, -1, -1):
        for j in range(10):
            if (arr[i + 1] + j) % 2 == 0:
                dp[i][j] = dp[i + 1][(arr[i + 1] + j) // 2]
            else:
                dp[i][j] = dp[i + 1][(arr[i + 1] + j) // 2] + dp[i + 1][(arr[i + 1] + j + 1) // 2]
    ownIn = 1
    for i in range(n - 1):
        if (arr[i] + arr[i + 1]) != arr[i + 1] * 2 and (arr[i] + arr[i + 1]) != arr[i + 1] * 2 - 1:
            ownIn = 0
    print(sum(dp[0]) - ownIn)