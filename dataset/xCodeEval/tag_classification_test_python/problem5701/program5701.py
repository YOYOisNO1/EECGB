def program5701():
    from fractions import *
    x, y, n = map(int, input().split())
    r = Fraction(x, y).limit_denominator(n)
    print('%d/%d') % (r.numerator, r.denominator)