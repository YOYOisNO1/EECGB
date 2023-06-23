def program1738():
    n = int(input())
    sqrt = int(n ** (1/2))
    2x = sqrt * sqrt
    r = None
    
    if not n - 2x:
        r = 2 * sqrt
    elif n - 2x > sqrt:
        r = 2 * sqrt + 1
    r = 2 * sqrt + 2
    print(r)