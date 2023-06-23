    from math import factorial
    from collections import defaultdict
def main():
        n, k, s = map(int, input().split())
        a = map(int, input().split())
    def f(b):
            res = defaultdict(int)
            res[0] = 1
            for x in b:
                nr = defaultdict(int)
                for y, t in res.viewitems():
                    if x <= 18:
                        nr[factorial(x) + y] += t
                    nr[x + y] += t
                    nr[y] += t
                res = nr
            return res
    def g(b):
            res = defaultdict(int)
            res[s] = 1
            for x in b:
                nr = defaultdict(int)
                for y, t in res.viewitems():
                    if x <= 18:
                        nr[y - factorial(x)] += t
                    nr[y - x] += t
                    nr[y] += t
                res = nr
            return res
        dl = f(a[:n/2])
        dr = g(a[n/2:])
        b = set(dl.keys() + dr.keys())
        ans = 0
        for x in b:
            ans += dl[x] * dr[x]
        print ans
    main()