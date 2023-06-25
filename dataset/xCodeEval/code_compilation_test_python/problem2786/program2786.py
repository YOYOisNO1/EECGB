def program2786():
    from fractions import Fraction
    a, b,d = map(int, input().split(' '))
    f = Fraction(a, b).limit_denominator(d)
    x = f.numerator
    y = f.denominator
    print str(x)+'/'str(y);