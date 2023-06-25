    n, m = map(int, input().split())
    a = [[3, 2], [0, 1]]
def mul(p, q):
        global m
        res = [[0, 0], [0, 0]]
        for i in xrange(2):
            for j in xrange(2):
                for k in xrange(2):
                    res[i][j] += p[i][k] * q[k][j]
                    res[i][j] %= m
        return res
def mpow(p, k):
        if k == 0:
            return [[1, 0], [0, 1]]
        if k == 1:
            return p
        tmp = mpow(p, k/2)
        res = mul(tmp, tmp)
        if k & 1:
            res = mul(res, p)
        return res
    t = mpow(a, n-1)
    print t[0][0] * 2 + t[0][1]