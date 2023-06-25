def program3352():
    n, s = map(int, input().split())
    lo, hi = 1, n + 1
    while lo < hi:
        mid = (lo + hi) / 2
        if mid - sum(map(int, list(str(mid)))) >= s:
            hi = mid
        else:
            lo = mid + 1
    print(n) - lo + 1