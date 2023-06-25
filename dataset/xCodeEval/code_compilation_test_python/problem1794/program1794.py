def program1794():
    import sys
    a, b = [int(x) for x in input().split()]
    if a=b:
      print("YES")
      sys.exit()
    if a>b:
      if a-b==1:
        print("YES")
      else: 
        print("NO")
    else:
      if b-a==1:
        print("YES")
      else:
        print("NO")