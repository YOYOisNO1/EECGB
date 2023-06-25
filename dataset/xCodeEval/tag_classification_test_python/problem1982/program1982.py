def okay(n, m, k, v):
        total = n * v
        if k <= v:
            total -= k * (k-1) // 2
        else:
            total -= v * (v-1) // 2
            total -= (k-v) * (v-1)
        if n-k+1 <= v:
            total -= (n-k) * (n-k+1) // 2
        else:
            total -= v * (v-1) // 2
            total -= (n-k-v+1) * (v-1)
        return m >= total
    
    n, m, k = map(int, input().split())
    ans = 1
    low, up = 1, 1000000000
    while low <= up:
        mid = (low + up) // 2
        if okay(n, m, k, mid):
            ans, low = mid, mid + 1
        else:
            up = mid - 1
    
    print(ans)