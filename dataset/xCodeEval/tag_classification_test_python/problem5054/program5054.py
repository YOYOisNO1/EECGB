def program5054():
    c = lambda:map(int, input().split())
    n, m = c()
    a = c()
    print([(m) - sum(a)) / 5, -1][m < sum(a) + (n - 1) * 10]