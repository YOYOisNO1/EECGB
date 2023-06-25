def program5752():
    from fractions import Fraction
    x,y,n = [int(x) for x in input().split()]
    ans = Fraction(x,y).limit_denominator(n)
    print(str(ans.numerator)+'/'+str(ans.denominator))