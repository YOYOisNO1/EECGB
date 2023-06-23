def program1867():
    s = input()
    n = s.split()[0]
    k = int(s.split()[1])
    ret = 100
    for mask in xrange(2 ** len(n)):
        t = ""
        for i in xrange(len(n)):
            if mask & (2**i):
                t += s[i]
        if int(t) % (10**k) == 0:
            ret = min(ret, len(t)
    print ret