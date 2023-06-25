def program3396():
    a = [input().count('B') for i in xrange(8)]
    print((min(a)) & 7) + a.count(8)