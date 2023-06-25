def program4841():
    n, s = input().split(' ')
    
    n = int(n)
    s = int(s)
    
    if n >= s:
      print(1)
    else:
      if s%n != 0:
        print(s//n+1)
      else:
        print(s//n)