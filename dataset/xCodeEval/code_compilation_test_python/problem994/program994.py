def program994():
    =int(input().strip())
    a = [0, 0, 0]
    a[0] = int(input().strip())
    a[1] = int(input().strip())
    a[2] = int(input().strip())
    ans = 0
    if min(a) not in a[:2]:
        ans = min(a[:2]) + max(n - 2, 0)*min(a)
    else:
        ans = max(n - 1, 0)*min(a)
    if n == 1:
        ans = 0
    print(ans)