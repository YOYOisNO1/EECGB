    import sys
    
    b, d = [int(s) for s in sys.stdin.readline().split(' ')]
    
def pf(d):
        l = []
        i = 2
        while i * i <= d:
            if d % i == 0:
                while d % i == 0: d /= i
                l.append(i)
        if i > 1:
            l.append(i)
        return l
    
def typ(b, d):
        if (b ** 7) % d == 0:
            i, bb = 1, b
            while bb % d != 0:
                i, bb = i + 1, bb * b
            return (2, i)
        elif (b - 1) % d == 0:
            return 3
        elif (b + 1) % d == 0:
            return 11
        else:
            p = pf(d)
            if p and all(typ(b, f)[0] != 7 for f in p):
                return 6
            else:
                return 7
    
    t=typ(b,d)
    if isinstance(t, int):
        print "%d-type" % t
    else:
        print "%d-type" % t[0]
        print t[1]