def program1036():
    x = map(int, input().split())
    x = sorted(x)
    print((x[1]) - x[0]) + (x[2] - x[1])