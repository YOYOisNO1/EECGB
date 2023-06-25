def program48():
    n = int(input())
    m = (10 ** 9 + 7)
    fact = 1
    result = 1
    t = n
    while t:
        result = (result * t) % m
        t -= 1
        fact += 1
    
    print(int((m + result - (2 ** (n - 1)) % m) % m))