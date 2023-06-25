def program3061():
    a, b, c, d, e, f = [int(x) for x in list(input().split())]
    print((a + b + c) ** 2 - a ** 2 - c ** 2 - e ** 2)