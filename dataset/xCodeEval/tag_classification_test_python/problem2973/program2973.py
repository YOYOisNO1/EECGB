def program2973():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    sumi = [0 for i in range(n)]
    sumi[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        sumi[i] = sumi[i+1]+arr[i]
    
    dp = [[[0, 0], [0, 0]] for i in range(n+1)]
    
    dp[n-1][0] = [arr[-1], 0]
    dp[n-1][1] = [0, arr[-1]]
    for i in range(n-2, -1, -1):
        for j in range(i, n):
            # 0 turn
            c1 = arr[j] + dp[j+1][1][0]
            if c1 > dp[i][0][0]:
                dp[i][0] = [c1, sumi[i]-c1]
            
            #1 turn
            c2 = arr[j] + dp[j+1][0][1]
            if c2 > dp[i][1][1]:
                dp[i][1] = [sumi[i]-c2, c2]
    
    print(*dp[0][1])
            