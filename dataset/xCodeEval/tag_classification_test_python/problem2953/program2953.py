def program2953():
    x, y = map(int, input ().split ())
    r = int((x * x + y * y) ** 0.5)
    print('black') if x * x + y * y == r * r or (r + (x > 0) + (y > 0)) % 2 == 0 else "white"