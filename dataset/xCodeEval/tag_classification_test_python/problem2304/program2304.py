    n = int(input())
    largest = -1
    ans = -1
    
def coprime(a, b):
      while a > 1:
        for k in range(2, a + 1):
          if a % k == 0:
            a /= k
            if b % k == 0:
              return False
            break
      return True
    
    for i in range(1, n):
      j = n - i
      if j > i:
        if coprime(i, j) and largest < float(i) / j:
          largest = float(i) / j
          ans = i
    
    print("%s %s" % (ans, n - ans))