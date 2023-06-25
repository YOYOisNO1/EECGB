def program5717():
    from fractions import Fraction
    x,y,n=map(int,input().split())
    f=Fraction(x,y).limit_denominator(n)
    if("/" not in str(f)):
        print(str(f)+"/1")
    else:
        print(f)