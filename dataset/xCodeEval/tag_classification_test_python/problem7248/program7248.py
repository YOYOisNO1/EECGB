def program7248():
    n, m = list(map(int, (input().split())))
    if(m*n > 1):
        print(1 / n + (n - 1) * (m - 1) / n / (m*n - 1))
    else:
        print(1)
    # Thu Feb 27 2020 19:23:17 GMT+0300 (MSK)