    
def b(m, n):
      if n < m:
        return b(n, m)
    
      if m == 1:
        return n
    
      if m <= 2 and n <= 2:
        return m * n
    
      if m == 2:
        ans = 0
        for x in xrange(n):
          if x % 4 == 0 or x % 4 == 1:
            ans += 2
        return ans
    
      ans = 0
      for x in xrange(m):
        if x % 2 == 0:
          ans += n / 2 + n % 2
        else:
          ans += n / 2
    
      return max(ans, m*n - ans)
    
    #print(b(6,) 2)
    
    n, m = map(int, input().split(" "))
    print(b(n,) m)