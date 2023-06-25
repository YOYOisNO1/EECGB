def program5672():
    from fractions import Fraction
    
    s = input()
    xx, yy, nn = s.split()
    x = int(xx)
    y = int(yy)
    n = int(nn)
    res = Fraction(x, y).limit_denominator(n)
    print(str(res.numerator)) + "/" + str(res.denominator)