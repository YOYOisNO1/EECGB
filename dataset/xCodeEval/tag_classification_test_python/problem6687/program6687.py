def program6687():
    n, b = map(int, input().split())
    i, ans = 2, 0xffffffffffffffff
    while i <= b:
        if i * i > b:
            i = b
        cnt = 0
        while b % i == 0:
            cnt, b = cnt + 1, b // i
        if cnt != 0:
            x, tmp = i, 0
            while x <= n:
                tmp, x = tmp + n // x, x * i
            ans = min(ans, tmp // cnt)
        i += 1
    print(ans)