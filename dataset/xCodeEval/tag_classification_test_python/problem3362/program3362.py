    luckies = []
    
def generate(s, n):
      if n != 0:
        a = 10 * s + 4
        b = 10 * s + 7
        luckies.append(a)
        luckies.append(b)
        generate(a, n - 1)
        generate(b, n - 1)
        
    generate(0, 10)
    luckies.sort()
    
    l, r = map(int, input().split())
    
    a = 0; b = len(luckies) - 1
    L = 0
    while a <= b:
      m = (a+b) // 2
      if luckies[m] >= l:
        L = m
        b = m - 1
      else:
        a = m + 1
        
    a = 0; b = len(luckies) - 1
    R = 0
    while a <= b:
      m = (a+b) // 2
      if luckies[m] >= r:
        R = m
        b = m - 1
      else:
        a = m + 1
        
    a = 0; b = len(luckies) - 1
    S = 0
    while a <= b:
      m = (a+b) // 2
      if luckies[m] <= r:
        S = m
        a = m + 1
      else:
        b = m - 1
    
    
    if S < L:
      res = (r - l + 1) * luckies[R]
    else:
      res = luckies[L] * (luckies[L] - l + 1) + luckies[R] * (r - luckies[S])
      for i in range(L, S):
        res += luckies[i+1] * (luckies[i+1] - luckies[i])
    print(res)
    
    """
def lucky(n):
      for digit in str(n):
        if digit not in '47':
          return False
      return True
    
    res = 0
    next_lucky = r
    while not lucky(next_lucky):
      next_lucky += 1
    for n in range(r, l-1, -1):
      if lucky(n):
        next_lucky = n
      res += next_lucky
      
    print(res)
    """
      
      
      
        