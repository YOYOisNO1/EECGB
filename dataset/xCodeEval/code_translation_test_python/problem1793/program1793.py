    
def solve(m, cubes, volume):
      if m == 0:
        return [cubes, volume]
    
      x = 1
      while (x ** 3) <= m:
        x += 1
      x -= 1
    
      best = solve(m - (x ** 3), cubes + 1, volume + x ** 3)
      if x > 1:
        best = max(best, solve((x ** 3) - 1 - ((x - 1) ** 3), cubes + 1, volume + (x - 1) ** 3))
    
      return best
    
    
    m = int(input())
    print(" ").join(map(str, solve(m, 0, 0)))
    #cubes = list(reversed([i * i * i for i in xrange(1, 20)]))
    
    