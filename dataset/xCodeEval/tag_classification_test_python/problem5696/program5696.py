def program5696():
    from fractions import *
    
    x,y,n=input().split()
    x=int(x)
    y=int(y)
    n=int(n)
    
    f=Fraction(x,y).limit_denominator(n)
    
    print(str(f.numerator)+"/"+str(f.denominator))