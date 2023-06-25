def program2213():
    x, y, a, b = map(int, input().split())
    
    gcd, d = x, y
    while d > 0:
        gcd, d = d, gcd % d
    
    lcm = x * y // gcd
    print(b//lcm - (a-1)//lcm)