def program447():
    r, h = map(int, input().split())
    r *= 2
    h *= 2
    q = (h / (r / 2) + 1) / 2
    xuy = h + r / 2 - (q * r - r / 2)
    xux = r / 2
    print(2) * q + (1 if xuy ** 2 + xux ** 2 >= r ** 2 else 0)
    