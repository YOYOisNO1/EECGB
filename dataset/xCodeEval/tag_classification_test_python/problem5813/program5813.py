    
    
def pred(n):
        f1 = n / x
        f2 = n / y
        both = n / x / y
        g1 = max(0, c1 - f2 + both)
        g2 = max(0, c2 - f1 + both)
        return g1 + g2 <= n - f1 - f2 + both
    
    c1, c2, x, y = map(int, input().split())
    
    l = 1
    r = 2
    while not pred(r):
        r *= 2
    
    while r - l > 1:
        mid = (l + r) / 2
        if pred(mid):
            r = mid
        else:
            l = mid
    print(r)