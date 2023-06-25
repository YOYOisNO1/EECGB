def _f(x):
        step = 0
        achieved = set([0])
        while x not in achieved and -x not in achieved:
            step += 1
            tmp = set()
            for cell in achieved:
                a = cell + step
                b = cell - step
                if b < 0: b *= -1
                tmp.add(a)
                tmp.add(b)
            achieved = tmp
            print achieved
        return step
    
def f(x):
        m = s = 0 if x%2 == 0 else 1
        while x > m or m%2 != x%2:
            s += 1
            m += s
        return s
    
    x = input()
    print "steps is %d"%f(x)