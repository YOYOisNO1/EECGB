def program1959():
    a, b, n, x = map(int, input().split())
    p = pow(a, n, 1000000007)
    print ((p * x) % 1000000007 + ((p - 1) / (a - 1) * b) % 1000000007) % 1000000007