def program5731():
    from fractions import Fraction
    x,y,n = map(int,input().split())
    a = x
    b = n
    
    z = Fraction(x,y).limit_denominator(n)
    print(z.numerator,z.denominator,sep='/')
    