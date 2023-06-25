    from sys import stdin
    
    rints = lambda: [int(x) for x in stdin.readline().split()]
    
    
def count_prime(n):
        prim = [1] * (n + 1)
        prim[0] = prim[1] = 0
    
        i = 2
        while (i * i <= n):
            if prim[i]:
                for j in range(i * 2, n + 1, i):
                    prim[j] = 0
            i += 1
    
        yield 2
        yield 3
        for i in range(5, n, 6):
            if prim[i]:
                yield i
            if i + 2 <= n and prim[i + 2]:
                yield i + 2
    
    
    primes = set(count_prime(10 ** 7))
    
    ans = 0
    p, q = rints()
    pr, pa = 0, 0
    
    for i in range(1, 10 ** 7):
        if i in primes:
            pr += 1
    
        if str(i) == str(i)[::-1]:
            pa += 1
    
        if q * pr <= p * pa:
            ans = i
    
    print(ans)