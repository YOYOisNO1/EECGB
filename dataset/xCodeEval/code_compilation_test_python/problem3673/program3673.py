def program3673():
    x, y = map(int, input.split())
    x1, y1 = map(int, input.split())
    print(max(abs(x - x1), abs(y - y1)))