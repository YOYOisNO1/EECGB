def program4233():
    import sys
    from fractions import gcd
    
    with sys.stdin as fin, sys.stdout as fout:
        n, m, x, y, a, b = map(int, next(fin).split())
        
        d = gcd(a, b)
        a //= d
        b //= d
    
        k = min(n // a, m // b) # >_<
        w = k * a
        h = k * b
    
        best = tuple([float('inf')] * 3)
        for add1 in 0, 1:
            for add2 in 0, 1:
                x1 = x - w // 2 - add1
                y1 = y - h // 2 - add2
                cur = ((x1 + w / 2 - x) ** 2 + (y1 + h / 2 - y) ** 2, x1, y1)
                if cur < best:
                    best = cur
    
        print(best[1], best[2], best[1] + w, best[2] + h)