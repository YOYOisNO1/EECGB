    import sys
                      
def go (n, r, p): 
      ret = 0
      r = min (r, p)
      while n > 0:
        if r > p / 2:
          ret += n % 2
          r -= 1
        if r >= p / 2:
          ret += n / 2
          r -= p / 2
        n /= 2
        p /= 2
      return ret
    
    
    for line in sys.stdin:
      n, l, r = map (int, line.split())
      p = 1
      while p < n:
        p = p * 2 + 1
      print((go) (n, r, p) - go (n, l-1, p))
    
    
    