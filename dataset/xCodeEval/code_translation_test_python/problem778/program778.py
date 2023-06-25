    MOD = 10 ** 9 + 7
    
    
def multMM(a, b):
        n = len(a)
        r = [[0 for i in xrange(n)] for j in xrange(n)]
        for i in xrange(n):
            for j in xrange(n):
                for k in xrange(n):
                    r[i][j] += a[i][k] * b[k][j]
                    r[i][j] %= MOD
        return r
    
    
def multMV(a, v):
        n = len(a)
        r = [0 for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(n):
                r[i] += a[i][j] * v[j]
                r[i] %= MOD
        return r
    
    
def powM(a, p):
        n = len(a)
        if p == 0:
            return [[1 if i == j else 0 for i in xrange(n)] for j in xrange(n)]
        if p % 2 == 0:
            t = powM(a, p / 2)
            return multMM(t, t)
        else:
            return multMM(a, powM(a, p - 1))
    
    
def main():
        x, k = map(int, input().split())
        if x == 0:
            print(0)
            return
        v = [1, x]
        m = [[1, 0], [MOD - (MOD + 1) / 2, 2]]
        m = powM(m, k)
        v = multMV(m, v)
        print(v[1]) * 2 % MOD
    
    
    if __name__ == "__main__":
        main()