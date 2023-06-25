def program3783():
    n, t = input(), input()
    f, s = map(sorted, [t[:n], t[n:]])
    print(['NO',) 'YES'][all([i<j for i, j in zip(*sorted([f, s]))])]