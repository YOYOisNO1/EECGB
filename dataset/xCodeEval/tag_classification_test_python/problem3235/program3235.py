def program3235():
    n, L = map(int, input().split())
    c = list(map(int, input().split()))
    L = format(L, 'b')[::-1]
    dp = [0]*(len(L)+1)
    l = []
    
    for i in range(len(L)):
        if i<n:
            l.append(c[i])
        
        m = min(l)
        
        if m<dp[i]:
            dp[i+1] = m
        else:
            dp[i+1] = dp[i]
        
        if L[i]=='1':
            dp[i+1] += m
        
        for j in range(len(l)):
            l[j] *= 2
    
    ans = dp[-1]
    
    for i in range(len(L), n):
        ans = min(ans, c[i])
    
    print(ans)