def program1936():
    x = input()
    vals = [int(v) for v in x.split()]
    a = range(vals[0], vals[1] + 1)
    if a[-1] > vals[1]:
        print a[-1] - vals[1]
    else
        print 0