    n = int(input())
    
def isprime(n) :
        for i in range(1, n + 1) :
            if i * i > n :
                return 1
            elif n % i > 0 :
                return 0
        return 0   
    if isprime(n) == 1 :
        print(1)
    elif n % 2 == 0 || isprime(n - 2) == 1 :
        print(2)
    else :
        print(3)