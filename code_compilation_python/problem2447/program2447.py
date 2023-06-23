    n = int(input())
    
def is_prime(x):
        for i in range(2, round(x ** 0.5)):
            if x % i == 0:
                return False
        return True
    
    
    if is_prime(n):
        print(1)
    elif n % 2 == 0:
        print(2):
    else:
        print(3)