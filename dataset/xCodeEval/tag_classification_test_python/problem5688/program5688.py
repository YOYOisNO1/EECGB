    #coding=utf-8
    import math
    x, y, n = map(int, input().split())
    a, b = 1000000, 1000000
    res = 100000000.0
    
def sgn(num):
        '''
            居然要这么高的精度才能过！
        '''
        eps = 1e-15
        return (num > eps) - (num < -eps)
    
def deal(ta, tb):
        global res
        global a
        global b
        d = abs(x/(y + 0.0) - ta/(tb + 0.0))
        if sgn(d - res) == -1:
            res = d
            a, b = ta, tb
        elif sgn(d - res) == 0:
            if tb < b:
                a, b = ta, tb
            elif tb == b and ta < a:
                a, b = ta, tb
    
    for i in xrange(1, n+1):
        t = x*i / (y + 0.0)
        tc = int(math.ceil(t))
        tf = int(math.floor(t))
        deal(tc, i)
        deal(tf, i)
    
    print(str(a)) + '/' + str(b)