def program4030():
    w, x = map(int, input().split())
    a = []
    cur = w ** 50
    while cur:
        if x >= cur:
            a.append(x // cur)
            x %= cur
        else:
            a.append(0)
        cur //= w
    for i in range(50, 1, -1):
        if a[i] > 1:
            a[i] -= w
            a[i - 1] += 1
        if a[i] not in {-1, 0, 1}:
            print("NO")
            exit(0)
    print("YES")