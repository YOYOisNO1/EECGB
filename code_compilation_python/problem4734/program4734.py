    import math
    from operator import mul
def comb(i, j):
        if j > i or j < 0: return 0
        return reduce(mul, xrange(i, i - j, -1), 1)/reduce(mul, xrange(1, j+1), 1)
    
def g(r, p, k):
        s = 0
        p2 = 2 ** p
        while r > 0:
            while r < p2:
                p2 /= 2
                p -= 1
            s += comb(p, k)
            r -= p2
            k -= 1
            if k < 0: break
        return s
    
    n, t = map(int, input().split())
    if math.log(t, 2) - int(math.log(t, 2)) > 1e-5:
        print 0
    else:
        n += 1
        k = int(math.log(t, 2))
        p = int(math.log(n + 1, 2)) - 1
        ans = comb(p+1, k+1) + g(n - 2**(p+1) + 1, p, k)
        if t == 1: ans -= 1
        print ans