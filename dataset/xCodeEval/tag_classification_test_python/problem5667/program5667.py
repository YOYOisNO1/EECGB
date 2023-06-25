def program5667():
    from fractions import Fraction
    a, b, d = map(int, input().split(' '))
    f = Fraction(a, b).limit_denominator(d)
    num = f.numerator
    den = f.denominator
    print(str(num) + '/' + str(den))