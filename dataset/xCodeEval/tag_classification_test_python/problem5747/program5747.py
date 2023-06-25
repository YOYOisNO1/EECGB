def program5747():
    from fractions import Fraction
    a,b,c=[int(i) for i in input().split()]
    frac=Fraction(a,b).limit_denominator(c)
    print(str(frac.numerator)+'/'+str(frac.denominator))