def f(n, k):
        n0, s = n, 0
        while n > 0:
            s += min(n, k)
            n -= min(n, k)
            n -= n // 10
        return s * 2 >= n0
    
    
def g(n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if f(n, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    print(g(int(input())))