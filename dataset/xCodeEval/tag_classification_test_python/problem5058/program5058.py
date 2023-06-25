def program5058():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    if ((n - 1) * 10 + s > d):
        print(-1)
    else:
        print((n-1)*2 + (d - (n - 1) * 10 - s) // 5)