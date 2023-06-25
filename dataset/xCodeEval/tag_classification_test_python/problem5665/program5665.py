def program5665():
    from fractions import Fraction
    x, y, n = map(int, input().split())
    f = Fraction(x, y).limit_denominator(n)
    a = f.numerator
    b = f.denominator
    print(str(a)) + "/" + str(b)
    