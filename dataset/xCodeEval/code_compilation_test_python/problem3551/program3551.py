    #!/usr/bin/python3
    
def solve(n):
      if n == 0:
        return (0, 0)
      n -= 1
    
      x = 1
      y = 2
      c = 6
      k = 1
      while n >= c:
        x += 2
        n -= c
        c += 6
        k += 1
    
      lim = [k - 1] + [k] * 5
      dx = [-1, -2, -1, 1, 2, 1]
      dy = [2, 0, -2, -2, 0, 2]
    
      i = 0
      while n > 0:
        t = min(n, lim[i])
        x += t * dx[i]
        y += t * dy[i]
        n -= t
        i += 1
    
      return (x, y)
    
    x, y = solve(int(input()))
    print(x, y)
    # for i in range(21):
    #   print(i, solve(i))
    
    