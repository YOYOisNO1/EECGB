def program2243():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    f = 0
    s = 0
    for i in range(n - 1, -1, -1):
        if abs(f + a[i] - s) < abs(f - a[i] - s):
            f += a[i]
        else:
            s += a[i]
    print(abs(f - s))