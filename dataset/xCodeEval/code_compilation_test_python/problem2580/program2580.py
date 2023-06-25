def program2580():
    h1, h2 = map(int, input().split(" "))
    a, b = map(int, input().split(" "))
    day = 0
    c = h1
    while True:
      if day > 1 and b > a:
        day = -1
        break
      if day == 0:
        c += a * 8
      else:
        c += a * 12
      if c >= h2:
        break
      c -= b * 12
      day += 1
    print day
    