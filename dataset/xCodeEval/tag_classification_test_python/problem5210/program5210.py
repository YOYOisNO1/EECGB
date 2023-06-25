def program5210():
    import math
    n = int(input())
    c = 998244353
    ans, x, y = 0, 0, 2 ** n % c
    if n == 1 or n == 2:
        x = 1
    else:
        q, w = 1, 1
        for i in range(3, n + 1):
            q, w = w, (q + w) % c
        x = w
    z = math.gcd(x, y)
    x //= z
    y //= z
    ans = pow(y, c - 2, c)
    print((ans * x) % c)