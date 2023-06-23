def program780():
    r, x, y, p, q = list(map(int, input().strip().split(' '))
    print((((p - x) ** 2 + (q - y) ** 2) ** 0.5 + 2 * r - 1) // (2 * r))