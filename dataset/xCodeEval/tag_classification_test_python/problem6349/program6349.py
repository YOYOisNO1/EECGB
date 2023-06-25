    import sys
    import itertools
    import math
    import collections
    from collections import Counter
    
    #input = sys.stdin.readline
    
    #########################
    # imgur.com/Pkt7iIf.png #
    #########################
    
def sieve(n):
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        prime[0] = prime[1] = False
        r = [p for p in range(n + 1) if prime[p]]
        return r
def divs(n, start=1):
        r = []
        for i in range(start, int(math.sqrt(n) + 1)):
            if (n % i == 0):
                if (n / i == i):
                    r.append(i)
                else:
                    r.extend([i, n // i])
        return r
    
def flin(d, x, default = -1):
        f = l = -1
        for i in range(len(d)):
            if d[i] == x:
                if f == -1: f = i
                l = i
        if f == -1:
            return (default, default)
        else:
            return (f, l)
def ceil(n, k): return n // k + (n % k != 0)
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))
def lcm(a, b): return abs(a * b) // math.gcd(a, b)
def prr(a, sep=' '): print(sep.join(map(str, a)))
def dd(): return collections.defaultdict(int)
    
    pr = sieve(10**6 // 2)
def divn(n):
        res = 1
        for i in pr:
            if n == 1:
                return res
    
            t = 1
            while n % i == 0:
                t += 1
                n = n//i
            res *= t
    
    a, b, c = mi()
    mem = [0]*(10**6 + 1)
    res = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                n = i * j * k
                if mem[n] == 0: mem[n] = divn(i * j * k)
                res += mem[n]
    print(res % 1073741824)
    
    