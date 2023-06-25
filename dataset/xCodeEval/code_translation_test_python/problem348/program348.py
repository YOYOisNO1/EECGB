def program348():
    n, a, b, c, d = map(int, input().split())
    ans = n * (n - abs(a - d) - abs(b - c))
    print(max(0, ans))