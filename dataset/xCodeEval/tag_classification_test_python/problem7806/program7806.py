def program7806():
    pa, ta = map(int, input().split())
    pb, tb = map(int, input().split())
    h, s = map(int, input().split())
    
    ans = 10**18
    dp = [10**18] * (h+1)
    dp[0] = 0
    for hh in range(h+1):
        # propagate dp[hh]
        for _ in range(2):
            for i in range(1, h // (pa - s) + 5):
                now = i * ta
                j = now // tb
    
                nxt = hh + i * (pa - s) + j * (pb - s)
                if nxt >= h:
                    ans = min(ans, dp[hh] + now)
                
                if now >= tb:
                    nxt = hh + (i - 1) * (pa - s) + (j - 1) * (pb - s) + pa + pb - s
                    nxt = min(nxt, h)
                    dp[nxt] = min(dp[nxt], dp[hh] + now)
            
            pa, pb = pb, pa
            ta, tb = tb, ta
    
    # print(dp)
    
    ans = min(ans, dp[h])
    print(ans)