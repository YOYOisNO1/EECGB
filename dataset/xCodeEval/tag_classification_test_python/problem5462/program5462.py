def program5462():
    import math, sys
    from sys import stdin, stdout
    
    n, m, k, x, y = map(int, stdin.readline().strip().split(' '))
    if n <= 2:
      max_num = min_num = serj = k / (n * m)
      mod = k % (n * m)
      if mod:
        max_num += 1
        if mod >= (x - 1) * m + y:
          serj += 1
      print(max_num,) min_num, serj
      sys.exit()
    one_pass = (n - 1) * m #3762
    min_num = (k - one_pass - m) / (one_pass * 2) + 1
    max_num = (k - one_pass - m) / one_pass + 1
    if (k - one_pass - m) % one_pass:
      max_num += 1
    subtracted = k - (x - 1) * m - y #199706525
    if x == 1 or x == n:
      serj = subtracted / (one_pass * 2) + 1
    else:
      serj = subtracted / one_pass + 1
      if not serj % 2 and (n - x) * m * 2 > subtracted % one_pass + one_pass:
        serj -= 1
      elif serj % 2 and subtracted % one_pass >= (n - x) * m * 2:
        serj += 1
    print(max(1,) max_num), min_num, serj