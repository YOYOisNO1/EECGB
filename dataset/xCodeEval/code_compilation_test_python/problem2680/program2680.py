def program2680():
    [n, c] = map(int, input().split())
    a = map(int, input().split())
    r = []
    for i in range(1, n):
        v = a[i - 1] - a[i] - c
        if v >= 0:
            r.append(v)
    print max(r)