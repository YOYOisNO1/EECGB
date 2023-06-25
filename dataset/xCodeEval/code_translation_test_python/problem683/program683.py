def program683():
    n, m = map(int, input().split())
    mi, r, mx = n // m, n % m, n - m + 1
    print((m - r) * (mi * (mi - 1)) // 2 + r * ((mi + 1) * mi) // 2, (mx * (mx - 1)) // 2)