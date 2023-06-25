def program884():
    w, h, k = [int(x) for x in input().split()]
    s = 0
    for i in range(1, k + 1):
        s += (w - 4 * (i - 1) + h - 4 * (i - 1)) * 2 - 4
    print(s)