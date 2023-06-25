def program4771():
    n, m, i1, j1, i2, j2 = map(int, input().split())
    x = [abs(i1 - i2), abs(j1 - j2)]
    x.sort()
    if x[1] >= 5:
        print "Second"
    elif x[0] <= 2:
        print "First"
    else:
        if x[1] == 4:
            print "Second"
        else:
            print "First"