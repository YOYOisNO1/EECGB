def program241():
    n, k = map(int, input().split())
    
    
    left = 1
    right = 10**18 + 1
    
    p = [2**i for i in range(61)]
    
    ans = 0
    
    while right - left > 1:
        mid = (right + left) // 2
        l = 0
        r = 60
        if mid > n:
            right = mid
            continue
        while r - l > 1:
            m = (r + l) // 2
            if mid * p[m] <= n:
                l = m
            else:
                r = m
        cur = 0
        if mid % 2:
            cur += min(n - p[l] * mid + 1, p[l]) + p[l] - 1
        else:
            cur += p[l + 1] - 2 + min(n - p[l] * mid + 1, p[l + 1])
        if cur < k:
            right = mid
        else:
            ans = cur
            left = mid
    
    for i in range(0, 5000000):
        mid = left + i
        r = 60
        l = 0
        while r - l > 1:
            m = (r + l) // 2
            if mid * p[m] <= n:
                l = m
            else:
                r = m
        cur = 0
        if mid % 2:
            cur += min(n - p[l] * mid + 1, p[l]) + p[l] - 1
        else:
            cur += p[l + 1] - 2 + min(n - p[l] * mid + 1, p[l + 1])
        if cur >= k:
            left = mid
    
    print(left)