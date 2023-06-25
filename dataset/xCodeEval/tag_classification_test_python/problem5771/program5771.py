def program5771():
    from fractions import Fraction
    x, y, n = map(int, input().split())
    f, v, d = Fraction(x, y), Fraction(0), 100000
    for b in xrange(1, n + 1):
        a = b * x // y
        f1, f2 = Fraction(a, b), Fraction(a + 1, b)
        cd1, cd2 = abs(f1 - f), abs(f2 - f)
        if cd1 < d:
            v, d = f1, cd1
        if cd2 < d:
            v, d = f2, cd2
    print(str(v.numerator)) + '/' + str(v.denominator)