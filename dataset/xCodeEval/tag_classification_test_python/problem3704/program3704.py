def program3704():
    n, m = map(int, input().split())
    p = sorted((x[1], x[0]) for x in enumerate(map(int, input().split())))
    p = sorted((x[1], str(i % 2)) for i, x in enumerate(p))
    print(' '.join(x[1] for x in p))