def program1177():
    n, m, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l)
    ava = k
    i = n-1
    ans = 0
    result = False
    while i >= 0:
        if ava >= m:
            result = True
            break
        ava += (l[i]-1)
        i -= 1
        ans += 1
    if ava >= m:
        result = True
    if result:
        print(ans)
    else:
        print(-1)