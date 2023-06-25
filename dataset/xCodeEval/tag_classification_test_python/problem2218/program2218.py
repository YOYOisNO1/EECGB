    from functools import lru_cache
    from time import sleep
    
    INF = 1e100
    s = dict()
    # @lru_cache(None)
def solve(x, cur, k):
        if x in s:
            return s[x] + cur
        if len(str(x)) == k:
            return cur
        if len(str(x)) > k:
            return INF
        if x == 0 and k != 1:
            return INF
        ans = INF
        for i in str(x):
            if i != '1':
                ans = min(ans, solve(int(i) * x, cur + 1, k))
        s[x] = ans - cur
        return ans
    
    k, x = map(int, input().split())
    x = solve(x, 0, k)
    if x < INF:
        print(x)
    else:
        print(-1)