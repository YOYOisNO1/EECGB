def program4246():
    read = lambda: tuple(map(int, input().split()))
    x1, y1 = read()
    x2, y2 = read()
    l = (-1, 0, 1)
    ds = []
    dist = lambda a, b: max(a, b) - min(a, b)
    for i in l:
        for j in l:
            ds += [dist(x1, (x2+i)) + dist(y1, (y2+j))]
            
    print(min(ds) * 2 + 8)