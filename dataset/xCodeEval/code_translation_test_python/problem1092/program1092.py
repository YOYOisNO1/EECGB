def program1092():
    n, m, a, b = map(int, input().split())
    if b / m < a:
        print((n // m) * b + min((n % m) * a, b))
    else:
        print(n * a)