def program5502():
    n, h = map(int, input().split())
    t = s = [1] * (n + 1)
    for m in range(1, n + 1): s[m] = sum(s[m - 1 - k] * s[k] for k in range(m))
    for j in range(h): t = [sum((s[k] - t[k]) * t[m - 1 - k] + s[m - 1 - k] * t[k] for k in range(m)) for m in range(n + 1)]
    print(t[n])