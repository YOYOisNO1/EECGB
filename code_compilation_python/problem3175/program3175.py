def program3175():
    n, k, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = sum(a)
    
    maximum = 0
    i = 0
    while i < n and i * s <= m:
        cur = m - s * i
        ans = (k + 1) * i
        for i in range(k):
            if cur < a[i]:
                break
            c = min(n - i, cur // a[i])
            cur -= a[i] * c
            ans += c
        maximum = max(maximum, ans)
    
    print(maximum)