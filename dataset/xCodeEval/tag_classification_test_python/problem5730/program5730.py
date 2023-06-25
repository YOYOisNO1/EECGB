def program5730():
    from fractions import Fraction
    x,y,n = map(int,input().split())
    # if y<=n:
    #     b=Fraction(x,y)
    #     print('{}/{}'.format(b.numerator,b.denominator))
    # else:
    #     a=x/y
    #     b=Fraction(a).limit_denominator(n)
    #     print('{}/{}'.format(b.numerator,b.denominator))
    b=Fraction(x,y).limit_denominator(n)
    print('{}/{}'.format(b.numerator,b.denominator))