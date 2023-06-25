def program5759():
    from fractions import Fraction
    a,b,d=input().split()
    a=int(a)
    b=int(b)
    d=int(d)
    f=Fraction(a,b).limit_denominator(d)
    x=f.numerator
    y=f.denominator
    print(str(x)+'/'+str(y))