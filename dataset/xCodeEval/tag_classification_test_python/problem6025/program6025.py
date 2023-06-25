def program6025():
    n, m = map(int, input().strip().split())
    print((pow(3, n, m) - 1) % m)