    n, m, k = map(int, input().strip().split())
def fac(x):
        ret = 1
        for i in xrange(1, x + 1):
            ret *= i
        return ret
def c(n, r):
        return fac(n) / (fac(n - r) * fac(r)) if r <= n else 0
    print(c(n) - 1, k * 2) * c(m - 1, k * 2) % (10 ** 9 + 7)