def program5695():
    x,y,n = map(int, input().split())
    from fractions import Fraction
    f = Fraction(x,y).limit_denominator(n)
    print(str(f.numerator)) + "/" + str(f.denominator)