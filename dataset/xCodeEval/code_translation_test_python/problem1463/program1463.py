def program1463():
    from math import gcd
    n,m=map(int,input().split())
    lcm=n*m//(gcd(n,m))
    a,b=lcm//n,lcm//m
    # print()
    if abs(a-b)<=1:
        print("Equal")
    elif a>b:
        print("Dasha")
    else:
        print("Masha")
    