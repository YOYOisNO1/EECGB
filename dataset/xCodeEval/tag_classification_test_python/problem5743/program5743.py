def program5743():
    from fractions import Fraction as F
    
    a, b, n = map(int, input().split())
    frac = F(a, b).limit_denominator(n)
    print("{0}/{1}".format(frac.numerator, frac.denominator))