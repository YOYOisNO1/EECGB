def program5724():
    from fractions import Fraction as F
    
    x, y, n = map(int,input().split())
    fract = F(x, y).limit_denominator(n)
    print("/").join(map(str,(fract.numerator, fract.denominator)))