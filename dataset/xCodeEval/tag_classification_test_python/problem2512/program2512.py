    import math
    
    
def C(n,k):
        w=1
        for i in range(n-k+1,n+1):
            w*=i
        for i in range (1,k+1):
            w//=i
        return w
    
    
def multiples(limit):
        tmp = 1
        m = limit
        for j in range(2, limit + 1):
            no_multiples = 0
            while m % j == 0:
                no_multiples += 1
                m //= j
            if no_multiples:
                tmp *= C(no_multiples + k - 1, no_multiples)
    
        return tmp
    
    
    n, k = [int(x) for x in input().split(' ')]
    modulo = 1000000007
    total = 0
    for i in range(1, n+1):
        total += multiples(i)
    
    print(total % modulo)