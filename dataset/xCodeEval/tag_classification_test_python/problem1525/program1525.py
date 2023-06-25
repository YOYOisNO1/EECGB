def program1525():
    n, m, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))[::-1]
    cnt = 0
    while m > k:
        m -= k - 1
        try:
            k = a[0]
        except:
            print(-1)
            exit(0)
        a = a[1:]
        cnt += 1
    print(cnt)