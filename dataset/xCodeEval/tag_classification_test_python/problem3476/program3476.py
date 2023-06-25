def program3476():
    n, m = map(int, input().split())
    arr = [n // m] * m
    for i in range(1, n % m + 1):
        arr[i] += 1
    ost = [i for i in range(m)]
    ans = 0
    for x in ost:
        for y in ost:
            if (x ** 2 + y ** 2) % m == 0:
                ans += arr[x] * arr[y]
    print(ans)