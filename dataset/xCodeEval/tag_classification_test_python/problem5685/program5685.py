def program5685():
    from fractions import Fraction
    x,y,n=[int(x) for x in input().split()]
    fr=Fraction(x,y)
    fr=fr.limit_denominator(n)
    print(str(fr.numerator)+'/'+str(fr.denominator))