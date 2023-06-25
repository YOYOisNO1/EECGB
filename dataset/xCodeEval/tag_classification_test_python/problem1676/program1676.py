def program1676():
    n, m = map(int, input().split())
    if (m + n) < 10:
        x = (m + n) ** 2
    else:
        x = max(n, m)
    a = -1
    b = 0
    count = 0
    for i in list(range(x)):
        if a ** 2 + b == n and a + b ** 2 == m:
            a += 1
        else:
            a += 1
            for j in list(range(x)):
                if a ** 2 + b == n and a + b ** 2 == m:
                    count += 1
                    b += 1
                else:
                    b += 1
            b = 0
    print(count)