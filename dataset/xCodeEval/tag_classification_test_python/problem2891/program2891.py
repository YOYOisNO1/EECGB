def program2891():
    n, a, b = map(int, input().split())
    for i in range(abs(b)):
        if b < 0:
            a -= 1
            if a == 0:
                a = n
        if b >= 0:
            a += 1
            if a == n + 1:
                a = 1
    print(a)