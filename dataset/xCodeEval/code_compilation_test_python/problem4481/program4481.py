    from math import factorial
    from collections import defaultdict
def main():
        n, k, s = map(int, input().split())
        a = map(int, input().split())
    def f(b):
            res = [defaultdict(int) for _ in xrange(k + 1)]
            res[k][0] = 1
            for x in b:
                nr = [defaultdict(int) for _ in xrange(k + 1)]
                for j in xrange(k + 1):
                    for y, t in res[j].viewitems():
                        if j and x <= 18:
                            nr[j-1][factorial(x) + y] += t
                        nr[j][x + y] += t
                        nr[j][y] += t
                res = nr
            return res
    def g(b):
            res = [defaultdict(int) for _ in xrange(k + 1)]
            res[k][s] = 1
            for x in b:
                nr = [defaultdict(int) for _ in xrange(k + 1)]
                for j in xrange(k + 1):
                    for y, t in res[j].viewitems():
                        if j and x <= 18:
                            nr[j-1][y - factorial(x)] += t
                        nr[j][y - x] += t
                        nr[j][y] += t
                res = nr
            return res
        dl = f(a[:n/2])
        dr = g(a[n/2:])
        b = set()
        for i in xrange(k + 1):
            b.update(dl[i].keys())
            b.update(dr[i].keys())
        ans = 0
        for x in b:
            for i in xrange(k + 1):
                for j in xrange(k + 1):
                    if i + j <= k:
                        ans += dl[i][x] * dr[j][x]
        print ans
    main()