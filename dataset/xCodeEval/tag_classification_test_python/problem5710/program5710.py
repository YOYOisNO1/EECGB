def program5710():
    from fractions import  Fraction
    
    x,y,n = map(int, input().split())
    ans = Fraction(x,y).limit_denominator(n)
    s = ""
    s+=str(ans.numerator)
    s+="/"
    s+=str(ans.denominator)
    print(s)