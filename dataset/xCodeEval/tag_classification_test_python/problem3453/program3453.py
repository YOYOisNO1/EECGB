def program3453():
    c1 = int(input())
    c2 = int(input())
    c3 = int(input())
    c4 = int(input())
    
    cur = 2 * c1
    if cur == 0 and c3 >= 1:
      print(0)
    else:
      cur -= 2 * c4
      if cur == 0:
        print(1)
      else:
        print(0) 