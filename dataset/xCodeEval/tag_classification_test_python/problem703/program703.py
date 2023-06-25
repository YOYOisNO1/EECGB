def program703():
    from fractions import gcd
    a,b,x,y=map(int, input().split())
    gcd=gcd(x,y)
    x/=gcd
    y/=gcd
    print(x*(min(a/x,b/y)),y*min(a/x,b/y))