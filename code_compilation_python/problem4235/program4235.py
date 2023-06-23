def program4235():
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
                
                nxt += pa + pb - s
                nxt = min(nxt, h)
                dp[nxt] = min(dp[nxt], dp[hh] + now + tb - now%tb)
            
            nxt = min(h, hh + pa + pb - s)
            dp[nxt] = min(dp[nxt], dp[hh] + max(ta, tb))
            
            pa, pb = pb, pa
            ta, tb = tb, ta
    
    # print(dp)
    
    ans = min(ans, dp[h])
    print(ans)