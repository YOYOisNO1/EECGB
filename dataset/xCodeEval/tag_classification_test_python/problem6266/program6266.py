    md = 10**9 + 7
    
def mult(a, b):
        c = []
        nn, mm, pp = len(a), len(b[0]), len(a[0])
        for i in xrange(nn):
            c.append([])
            for j in xrange(mm):
                c[i].append(0)
                for k in xrange(pp):
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % md
        return c
    
def expo(M, e):
        if e == 0:
            return [[1, 0], [0, 1]]
        if e % 2 == 1:
            return mult(M, expo(M, e-1))
        else:
            t = expo(M, e / 2)
            return mult(t, t)
    
    n = input()
    print(mult([[1],[0]],) expo([[3, 1], [1, 3]], n))[0][0] % md