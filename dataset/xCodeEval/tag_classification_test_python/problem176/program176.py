def program176():
    s = input()
    n = len(s)
    
    dp = [0] * n
    ans = 0
    for i in range(n):
        for j in range(0,i):
            if s[i] == "A" and s[j] == "Q":
                dp[i] += 1
            if s[i] == "Q":
                ans += dp[j]
                
    print(ans)            