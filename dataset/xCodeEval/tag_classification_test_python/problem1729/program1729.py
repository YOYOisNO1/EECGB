def program1729():
    x, y = list(map(int, input().split()))
    a = 1 * (10 ** (x - 1))
    b = (1 * (10 ** x))
    c = 0
    for i in range(a, b):
        if (i % y) == 0:
            c += i
            break
    if c == 0:
        print(-1)
    else:
        print(c)