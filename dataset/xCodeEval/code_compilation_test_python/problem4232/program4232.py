def program4232():
    import sys
    from fractions import gcd
    
    with sys.stdin as fin, sys.stdout as fout:
        n, m, x, y, a, b = map(int, next(fin).split())
        
        d = gcd(a, b)
        a //= d
        b //= d
    
        k = n // max(a, b)
        w = k * a
        h = k * b
    
        x1 = x - (w + 1) // 2
        y1 = y - (h + 1) // 2
    
        print(x1, y1, x1 + w, y1 + h)