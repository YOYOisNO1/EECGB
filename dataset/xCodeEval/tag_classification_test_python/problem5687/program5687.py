def program5687():
    from fractions import Fraction as frac
    
    a, b, n = map(int, input().split())
    f = frac(a, b).limit_denominator(n)
    print(str(f.numerator)+'/'+str(f.denominator))