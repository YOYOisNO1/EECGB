def program1912():
    n, k = map(int,input().split())
    if k == 1:
      print(n)
    else:
      i = 0
      while (1 << i) < n: i++
      print (1 << i)