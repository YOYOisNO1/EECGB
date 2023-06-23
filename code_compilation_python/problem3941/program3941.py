    
def b(m, n):
      if m == 1:
        return n
    
      if n == 1:
        return m
    
      if m <= 2 and n <= 2:
        return m * n
    
      ans = 0
      for x in xrange(m):
        if x % 2 == 0:
          ans += n / 2 + n % 2
        else:
          ans += n / 2
    
      return max(ans, m*n - ans)
    
    
    n, m = map(int, input().split(" "))
    print b(n, m)