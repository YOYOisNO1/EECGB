    
def solve(offset, n):
      result = 0
      for day in range(offset, min(7, offset + n)):
        if day % 7 >= 5:
          result += 1
        n -= 1
      result += (n // 7) * 2
      for day in range(n % 7):
        if day % 7 >= 5:
          result += 1
      return result
    
    n = int(input())
    print('%d %d' % (solve(0, n), solve(5, n)))
    