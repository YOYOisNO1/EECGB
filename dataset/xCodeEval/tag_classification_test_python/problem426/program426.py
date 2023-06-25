def program426():
    import sys
    H, N = map(int, sys.stdin.readline().split())
    
    b = []
    n = N-1
    while n > 0:
      b.append(n%2)
      n /= 2
    while len(b) < H:
      b.append(0)
    b = reversed(b)
    di = 0
    level = H
    ans = 0
    for d in b:
      if d == di:
        ans += 1
        di = 1-di
      else:
        ans += 2**level
      level -= 1
    
    print(ans)
        
    
    