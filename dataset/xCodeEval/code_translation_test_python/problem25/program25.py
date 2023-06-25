def program25():
    for i in xrange(5):
        s = input().split()
        if '1' in s:
            t = i
            c = s.index('1')
    print(abs(2-t)+abs(c-2))