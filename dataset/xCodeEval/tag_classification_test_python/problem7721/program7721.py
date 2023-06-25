def program7721():
    from math import ceil
    
    n, m, s = [int(i) for i in input().split()]
    r = ceil(n / s) * (s if n % s == 0 else n % s)
    c = ceil(m / s) * (s if m % s == 0 else m % s)
    print(r * c)