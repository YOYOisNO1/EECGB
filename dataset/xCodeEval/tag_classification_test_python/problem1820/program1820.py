def program1820():
    import math
    
    n = int(input())
    
    t = 1
    while n > t * 5:
        n -= t * 5
        t *= 2
    
    if n <= 5:
        n -= 1
    print["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"][n / t]