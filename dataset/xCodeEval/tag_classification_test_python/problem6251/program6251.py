def program6251():
    n = int(input())
    mod = 10 ** 9 + 7
    x = 2
    b = 1
    for i in xrange(64):
        if n & (2 ** i): b = b * x % mod
        x = x * x % mod
    print((b) * (b + 1) / 2) % mod