def program5693():
    from fractions import Fraction
    x,y,n = map(int,input().split(' '))
    ans = Fraction(x,y).limit_denominator(n)
    print(str(ans.numerator)) + '/' + str(ans.denominator)