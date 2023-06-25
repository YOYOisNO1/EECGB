    import math
    
    
def isPrime(n):
        if n == 2: return True
        if n % 2 == 0: return False
        limit = math.isqrt(n)
        for i in range(3, limit + 1, 2):
            if n % i == 0:
                return False
        return True
    
    
    n, k = [int(item) for item in input().split()]
    ct, prev = 0, 2
    for i in range(3, n):
        if isPrime(i):
            temp = prev + i + 1;
            if isPrime(temp) and temp <= n:
                ct += 1
            prev = i
    
    print('YES' if ct >= k else 'NO')