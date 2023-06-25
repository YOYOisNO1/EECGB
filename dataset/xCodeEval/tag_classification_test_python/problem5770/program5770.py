def program5770():
    from fractions import Fraction as F
    
    a, b, t = map(int, input().split())
    frac = F(a, b).limit_denominator(t)
    print("{0}/{1}".format(frac.numerator, frac.denominator))