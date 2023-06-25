def program4553():
    n, x, y = map(int, input().split())
    f = lambda x: x in [n/2, n/2 + 1]
    print('NO') if f(x) and f(y) else 'YES'