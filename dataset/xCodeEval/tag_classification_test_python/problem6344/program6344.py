def program6344():
    import sys
    INF = 10**20
    MOD = 10**9 + 7
    I = lambda:list(map(int,input().split()))
    from math import gcd
    from math import ceil
    from collections import defaultdict as dd, Counter
    from bisect import bisect_left as bl, bisect_right as br
    
    
    """
    Facts and Data representation
    Constructive? Top bottom up down
    """
    a, b, c = I()
    MOD = 2 ** 30
    ans = 0
    
    primes = []
    for i in range(2, 100):
      for j in range(2, i):
        if i % j == 0:
          break
      else:
        primes.append(i)
    
    for i in range(1, a + 1):
      for j in range(1, b + 1):
        for k in range(1, c + 1):
          ok = i * j * k
          res = 1
          for p in primes:
            cnt = 0
            while ok % p == 0:
              ok //= p
              cnt += 1
            res *= (cnt + 1)
          ans += res
          ans %= MOD
    
    print(ans)