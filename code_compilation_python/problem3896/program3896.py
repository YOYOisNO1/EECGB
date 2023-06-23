def program3896():
    a, b, c, l = map(int, input().split())
    ans = (l + 3) * (l + 2) * (l + 1) // 3
    for z in (a, b, c):
        s = 2 * z - a - b - c
        for x in range(max(0, -s), (l - s) // 2 + 1):
            m = s + x
            ans -= (m + 1) * (m + 2)
        for x in range((l - s) // 2 + 1, l + 1):
            m = l - x
            ans -= (m + 1) * (m + 2)
    print(ans // 2)