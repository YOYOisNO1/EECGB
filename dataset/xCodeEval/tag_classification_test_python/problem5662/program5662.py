def program5662():
    import fractions as f
    x, y, n = map(int, input().split())
    a = str(f.Fraction(x, y).limit_denominator(n))
    print([a) + '/1', a]['/' in a]