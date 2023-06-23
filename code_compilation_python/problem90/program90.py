def program90():
    import sys
    import math
    from fractions import Fraction
    
    #sys.stdin = open('input.txt')
    
    t, w, b = map(int, input().split())
    
    m = int(w*b/math.gcd(w, b))
    ans = min(w, b) - 1 + (t//m)*(min(w, b))
    
    ans_frac = Fraction(ans, t)
    print('{}/{}'.format(ans_frac.numerator, ans_frac.denominator))