def program7569():
    R = lambda: map(int, input().split())
    n, k, m = R()
    dir = 'to tail' == input()
    for t, x in enumerate(map(int, input())):
        if m == 1:
            dir = 1
        elif m == n:
            dir = 0
        if not x:
            k = min(n, k + 1) if m < k else max(1, k - 1)
        else:
            k = 1 if dir else n
        m = m + 1 if dir else m - 1
        if k == m:
            print('Controller ' + str(t + 1))
            exit(0)
    print('Stowaway')