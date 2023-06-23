def program1976():
    from math import floor, ceil
    
    n, k = [int(x) for x in input().split()]
    
    r = floor(n / ceil(n / (k-1) 1e-5) + 1e-5)
    q = n // r
    x = q*k + r
    print(x)