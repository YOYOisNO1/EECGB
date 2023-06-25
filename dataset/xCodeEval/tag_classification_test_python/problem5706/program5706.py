def program5706():
    from fractions import Fraction
    
    x, y, n = map(int, input().split(' '))
    
    d = Fraction(x, y).limit_denominator(n)
    print(str(d.numerator)) + '/' + str(d.denominator)