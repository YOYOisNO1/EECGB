def program4230():
    x = int(input())
    if x > 3:
      if x % 2 == 0:
        print(str(x) + " 2")
      if x % 2 == 1:
        n = x - 1
        print(str(n) + " 2")
    elif x == 2 or x == 3:
      print("2 2")
    else:
      print("-1")