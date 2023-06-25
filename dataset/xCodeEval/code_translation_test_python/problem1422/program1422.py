def program1422():
    from sys import stdin, stdout
    
    n = int(stdin.readline())
    values = list(map(int, stdin.readline().split()))
    dp = [0 for i in range(n)]
    
    dp[-1] = values[-1]#сколько торта можно захавать, если прийдти туда с фишкой
    cnt = values[-1]
    
    for i in range(n - 2, -1, -1):
        cnt += values[i]
        dp[i] = max(dp[i + 1], cnt - dp[i + 1])
    
    stdout.write(str(cnt - dp[0]) + ' ' + str(dp[0]))