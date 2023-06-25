def program2613():
    n, a , b = map(int, input().split())
    lim = n - a
    c = 0
    for i in range(1, b + 2):
        if i <= n - a:
            c += 1
    print(c)