def program2211():
    from fractions import gcd
    [x,y,a,b]=[int(x) for x in input().split()]
    h=gcd(x,y)
    x=x//h
    y=y//h
    h=h*x*y
    print(int(b//h - (a-1)//h))