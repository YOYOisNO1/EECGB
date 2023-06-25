    n, s = map(int, input().split())
    
def dif(x):
        tmp = x
        while tmp > 0:
            x = x - tmp % 10
            tmp = tmp/10
        return x
    
    l = 0
    r = 2000000000000000000
    while l < r:
        m = (l + r)/2
        if dif(m) < s:
            l = m + 1
        else: r = m
    d = l
    
    while d % 10 > 0: d -= 1
    
    if n < d: print(0)
    else: print(n) - d + 1
        