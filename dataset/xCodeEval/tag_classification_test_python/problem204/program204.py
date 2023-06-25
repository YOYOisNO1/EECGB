def incr(t):
        m, s = map(int, t.split(':'))
        s += 1
        if s == 60:
            m += 1
            s = 0
        if m == 24:
            m = 0
        return '%02d:%02d' % (m, s)
    
def pain(t):
        return t[0] == t[4] and t[1] == t[3]
    
    t = input()
    for i in xrange(100000000):
        if pain(t):
            print(i)
            exit()
        t = incr(t)