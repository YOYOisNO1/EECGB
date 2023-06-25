def program265():
    a, b = map(str, input().split())
    i = 1
    ans = a[0]
    ok = False
    while i < len(a):
        if a[i] < b[0]:
            ans += a[i]
            i += 1
        else:
            ans += b[0]
            ok = True
            break
    if not ok:
        ans += b[0]
    print(ans)