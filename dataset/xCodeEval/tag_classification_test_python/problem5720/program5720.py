def program5720():
    from fractions import Fraction
    x,y,n = [int(x) for x in input().split()]
    f = Fraction(x,y).limit_denominator(n)
    print(str(f.numerator)+'/'+str(f.denominator))