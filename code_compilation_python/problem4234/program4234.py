def program4234():
    pa, ta = map(int, input().split())
    pb, tb = map(int, input().split())
    h, s = map(int, input().split())
     
    dp = [10**18] * (h+1)
    dp[0] = 0
    for hh in range(1, h+1):
        for _ in range(2):
            for i in range(hh//(pa - s) + 1):
                now = i * ta
                j = now // tb
                idx = hh - i * (pa - s) - j * (pb - s)
                if idx < 0:
                    dp[hh] = min(dp[hh], dp[max(idx, 0)] + now)
                
                nxt = max(ta, tb - now%tb)
                idx -= (pa + pb - s)
                dp[hh] = min(dp[hh], dp[max(idx, 0)] + now + nxt)
     
            pa, pb = pb, pa
            ta, tb = tb, ta
     
    # print(dp)
    print(dp[h])