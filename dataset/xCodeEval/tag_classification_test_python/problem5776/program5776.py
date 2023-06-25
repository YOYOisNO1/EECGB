def program5776():
    from __future__ import print_function
    from fractions import Fraction
    a, b, d = map(int, input().split())
    f = Fraction(a, b).limit_denominator(d)
    x = f.numerator
    y = f.denominator
    print(str(x)+'/'+str(y));