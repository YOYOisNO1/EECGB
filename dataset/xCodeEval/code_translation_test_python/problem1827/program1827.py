def program1827():
    n, m = map(int, input().split())
    if n * m == 1:
        print("%.12f") % 1.0
    else:
        print("%.12f") % (1.0 / n + 1.0 * (m - 1) / (n * m - 1) * (n - 1) / n)