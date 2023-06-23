    from fractions import gcd
def f(a, b, n, w):
        if n < 0:
            return w
        return f(a, b, n-gcd([a,b][w], n), !w)
    a, b, n = map(int, input().split())
    print [0, 1][f(a, b, n, 0)]