def program1793():
    import sys
    a, b = [int(x) for x in input().split()]
    if a=b:
      print("YES")
      sys.exit()
    if a>b:
      if (b-a)%2==1:
        print("YES")
      else: 
        print("NO")
    else:
      if (b-a)%2==1:
        print("YES")
      else:
        print("NO")