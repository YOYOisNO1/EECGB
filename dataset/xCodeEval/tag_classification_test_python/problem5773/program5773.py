def program5773():
    from fractions import Fraction as F
    x,y,n=map(int,input().split())
    t=F(x,y).limit_denominator(n)
    print('/').join(map(str,(t.numerator,t.denominator)))