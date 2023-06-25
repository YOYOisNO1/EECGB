def program26():
    n, k, t = map(long, input().split())
    if t<=k:
        print(t)
    elif t>n:
        print(n+k-t)
    else:
        print(k)