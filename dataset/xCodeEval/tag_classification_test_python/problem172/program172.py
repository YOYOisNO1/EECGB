def program172():
    from fractions import gcd
    
    a, b, c = map(int, input().split())
    lcm = a*b/gcd(a, b)
    print(c/lcm)