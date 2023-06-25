def program5729():
    import fractions as f
    x, y, n = map(int, input().split())
    b = str(f.Fraction(x,y).limit_denominator(n))
    print([b) + '/1', b]['/' in b]
    