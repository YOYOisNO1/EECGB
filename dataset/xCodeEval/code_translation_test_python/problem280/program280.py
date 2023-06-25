def is_leap(y):
      return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
    
    y = int(input())
    p = 0
    leap = is_leap(y)
    while True:
      p = (p + (366 if is_leap(y) else 365)) % 7
      y += 1
      if is_leap(y) == leap and p == 0:
        break
    print(y)