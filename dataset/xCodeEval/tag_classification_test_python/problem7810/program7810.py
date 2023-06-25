    import sys
    input = lambda: sys.stdin.readline().rstrip()
    INF = 10 ** 18
    
def solve():
    
    def search(x):
            low = 0
            high = 10 ** 18
            while low + 1 < high:
                m = (low + high) // 2
                if m // ta * (pa - s) + m // tb * (pb - s) >= x:
                    high = m
                else:
                    low = m
            return high
    
    
        pa, ta = map(int, input().split())
        pb, tb = map(int, input().split())
        h, s = map(int, input().split())
        
        dp = [INF] * (h + 1)
        dp[0] = 0
    
        for x in range(1, h + 1):
            m = search(x)
            dp[x] = m
            for i in range(1, x + 1):
                for _ in range(2):
                    if i * ta < m and i * ta >= tb:
                        damage = (i - 1) * (pa - s) + (i * ta - tb) // tb * (pb - s) + (pa + pb - s)
                        dp[x] = min(dp[x], i * ta + dp[max(0, x - damage)])
                    ta, tb, pa, pb = tb, ta, pb, pa
    
        return dp[h]
    
    print(solve())