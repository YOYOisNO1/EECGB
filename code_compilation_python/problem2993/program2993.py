def program2993():
    a, b, c, n = [int(x) for x in input().split())
    ans = n - ((a - c) + (b - c) +  c)
    if ans < 0:print(-1)
    else:print(ans)