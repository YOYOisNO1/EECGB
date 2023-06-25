    import math
    
def is_prime(n):
      if n < 2:
        return False
      for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
          return False
      return True
    
    primes = []
    for i in range(2, 1001):
      if is_prime(i):
        primes.append(i)
    
    primes2 = []
    for i in range(2, len(primes)):
      for j in range(i - 1):
        if primes[j] + primes[j+1] + 1 == primes[i]:
          primes2.append(primes[i])
    
    n, k = map(int, input().split())
    cnt = 0
    for x in primes2:
      if x <= n:
        cnt += 1
      else:
        break
    
    if cnt >= k:
      print('YES')
    else:
      print('NO')