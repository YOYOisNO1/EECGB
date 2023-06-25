    # Let dp[i][x] = the biggest height you can get with width x using i extensions
    
    
def check(xx, yy):
        global a, b
        return (xx >= a and yy >= b) or (xx >= b and yy >= a)
    
    
    MAX_SIZE = 10 ** 5 + 1
    
    a, b, h, w, n = map(int, input().split())
    
    if check(h, w):
        print(0)
        exit(0)
    
    ext = map(int, input().split())
    ext.sort(reverse=True)
    ext = ext[:34]
    
    i = 1
    prev_dp = {}
    dp = {}
    
    prev_dp[w] = h
    for i in xrange(0, len(ext)):
        for k in prev_dp:
            dp[k] = prev_dp[k] * ext[i]
            t = min(k * ext[i], MAX_SIZE)
            dp[t] = max(dp.get(t, 0), prev_dp[k])
            if check(k, dp[k]) or check(t, dp[t]):
                print(i) + 1
                exit(0)
    
        # for x in xrange(MAX_SIZE):
        #     dp[x] = prev_dp[x] * ext[i]
        #     if x % ext[i] == 0:
        #         dp[x] = max(dp[x], prev_dp[x / ext[i]])
        #     if check(x, dp[x]):
        #         print(i) + 1
        #         exit(0)
        prev_dp = dp
        dp = {}
    
    print(-1)