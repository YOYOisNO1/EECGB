def program3241():
    n = int(input())
    be, en, ans = 8, 8 * 10 ** 15, float('inf')
    all = [x * x * x for x in range(2, 200001)]
    
    while be <= en:
        cur, md, k = 0, (be + en) >> 1, 0
    
        while all[k] <= md:
            cur += md // all[k]
            k += 1
    
        if cur < n:
            be = md + 1
        else:
            if cur == n:
                ans = min(ans, md)
            en = md - 1
        # print(cur,ans,md)
    
    print(-1 if ans == float('inf') else ans)