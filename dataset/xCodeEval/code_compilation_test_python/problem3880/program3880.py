def program3880():
    from fractions import Fraction
    a, b, x, y = list(map(int, input().split()))
    
    pocz = 1
    kon = 1e18+5
    srd = 0
    f = Fraction(x, y)
    
    while kon - pocz > 1:
        srd = (kon + pocz) // 2
    
        if f.numerator * srd <= a and f.denominator * srd <= b:
            pocz = srd
        else:
            kon = srd
    
    if srd == 2:
        if f.numerator * 2 <= a and f.denominator * 2 <= b:
            pass
        elif f.numerator <= a and f.denominator <= b:
            srd = 1
        else:
            srd = 0
    
    print(int(srd))