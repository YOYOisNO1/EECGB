def program3070():
    
    #code
    n = int(input())
    s = input()
    fl = True
    dp = [1]*n
    for i in range(1,n):
        for j in range(i):
            if s[j] > s[i]:
                dp[i] = max(dp[i],1+dp[j])
    for i in dp:
        if i>=3:
            fl = False
            break
    if not fl:
        print("NO")
    else:
        ans = "0"
        prev = s[0]
        for i in range(1,n):
            if s[i]<= prev:
                ans += "1"
            else:
                ans += "0"
            prev = s[i]
        print("YES")
        print(ans