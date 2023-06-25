    import math
    # A function to print(all) prime factors of
    # a given number n 
def primeFactors(n):
        a = []
        # Print the number of two's that divide n
        while n % 2 == 0:
            a.append(2)
            n //= 2
    
        # n must be odd at this point 
        # so a skip of 2 ( i = i + 2) can be used 
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            # while i divides n , print(i) ad divide n 
            while n % i == 0:
                a.append(i)
                n //= i
                # Condition if n is a prime
        # number greater than 2 
        if n > 2:
            a.append(n)
        return sorted(list(set(a)))
    
    n = int(input())
    if n==1:
        print(n)
    else:
        pfs = primeFactors(n)
        if len(pfs)==1:
            print(pfs[0])
        else:
            print(1)