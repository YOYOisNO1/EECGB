def program2799():
    w, h = [int(s) for s in input().split(' ')]
    u1, d1 = [int(s) for s in input().split(' ')]
    u2, d2 = [int(s) for s in input().split(' ')]
    if d1 > d2:
        for i in range(h, d1 - 1, -1):
            w += i
        w = max(0, w - u1)
        for i in range(d1 - 1, d2 - 1, - 1):
            w += i
        w = max(0, w - u2)
        for i in range(d2 -1, 0, - 1):
            w += i
    else:
        for i in range(h, d2 - 1, -1):
            w += i
        w = max(0, w - u2)
        for i in range(d2 - 1, d1 - 1, - 1):
            w += i
        w = max(0, w - u1)
        for i in range(d1 -1, 0, - 1):
            w += i
    print(w)