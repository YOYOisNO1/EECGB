def program5691():
    from fractions import Fraction
    x, y, n = map(int, input().split(' '))
    f = Fraction(x, y).limit_denominator(n)
    x = f.numerator
    y = f.denominator
    print(str(x)+'/'+str(y))