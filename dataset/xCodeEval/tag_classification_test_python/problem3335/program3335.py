    n = int(input())
    
    import math
def isPrime(x):
        for i in range(2, min(x, 10 ** 5)):
            if x % i == 0:
                return False
            
        return True
    
    if isPrime(n):
        print(1)
    elif isPrime(n - 2):
        print(2)
    elif n & 1:
        print(3)
    else:
        print(2)