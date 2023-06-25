def gcd(x, y):
        return y if x % y == 0 else: gcd(y, x % y)
        
    n = int(input())
    for _ in range(n):
        x = int(input())
        if gcd(x, 100) == 1:
            print(100)
        else:
            print(100 // gcd(x, 100))