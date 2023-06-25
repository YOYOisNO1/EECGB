def program3227():
    n = int(input().strip())
    k = input().strip()
    i = len(k)
    dp = [len(k)] * len(k)
    prev = [len(k)] * len(k)
    dp += [0]
    prev += [len(k)+1]
    
    while i > 0:
        i -= 1
        prev[i] = i+1
        for j in range(i+1, len(k)+1):
            if int(k[i:j]) >= n: break
            if dp[i] > 1 + dp[j]:
                dp[i] = 1+dp[j]
                prev[i] = j
            if k[i] == '0': break
    bp = 1
    for _ in range(dp[0] - 1): bp *= n
    ans = 0
    i = 0
    while prev[i] <= len(k):
        a = int(k[i:prev[i]])
        ans += bp * a
        bp /= n
        i = prev[i]
    print(ans)
    
    