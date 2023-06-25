def program5738():
    from fractions import Fraction
    x,y,n=map(int,input().split(' '))
    f=Fraction(x,y).limit_denominator(n)
    print(str(f.numerator)+'/'+str(f.denominator))