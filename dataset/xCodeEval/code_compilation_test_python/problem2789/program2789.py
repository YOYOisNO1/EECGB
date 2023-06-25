def program2789():
    from fractions import Fraction
    from __future__ import print_function
    a, b, d = map(int, input().split())
    f = Fraction(a, b).limit_denominator(d)
    x = f.numerator
    y = f.denominator
    print(str(x)+'/'+str(y));