def program5727():
    from fractions import Fraction
    
    x, y, n = map(int, input().split())
    val = Fraction(x, y)
    ret = val.limit_denominator(n)
    print('%d/%d' % (ret.numerator, ret.denominator))