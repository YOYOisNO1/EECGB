    n, k = map(int, input().split())
def f(m): return k*(k-1)/2-(k-m)*(k-m-1)/2+1
    if f(k - 1) < n:
        print(-1)
    else:
        l, h = 0, k - 1
        while l < h:
            m = (l + h) / 2
            if f(m) < n: l = m + 1
            else: h = m
        print(l)