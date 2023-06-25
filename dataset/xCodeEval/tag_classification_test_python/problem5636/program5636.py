def program5636():
    x, y = map(int, input().split())
    x, y = min(x, y), max(x, y)
    ans = x * y
    if x == 1:
        ans = y
    elif x == 2:
        ans = 2 * (y // 4 * 2 + min(y % 4, 2))
    else:
        ans = (x * y + 1) // 2
    print(ans)