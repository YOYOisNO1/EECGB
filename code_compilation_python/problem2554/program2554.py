def program2554():
    import sys
    
    (a, b) = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    if len(b - a) >= 10:
      print(0)
    input = [x%10 for x in range(a + 1, b + 1)]
    else:
      result = 1
      for x in input:
          result *= x
          result %= 10
          
      print(result)