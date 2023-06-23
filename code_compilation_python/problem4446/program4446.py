def program4446():
    n = int(input())
    m = int(1e9 + 7)
    # binom(2n - 1, n)
    p = 1
    for i in range(1, n + 1):
        p  *= 2 * n - i
        p //= i
        p  %= m
    print((2 * p - n) % m)