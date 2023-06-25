def program5760():
    from fractions import Fraction
    a,b,c=map(int,input().split())
    z=f'{Fraction(a,b).limit_denominator(c)}'
    if '/' not in z:print(z+'/1')
    else: print(z)