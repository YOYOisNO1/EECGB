def program1208():
    t = int(input())
    for i in range(t):
      a = list(map(int,input().strip().split()))[:2]
      b = list(map(int,input().strip().split()))[:2]
      if a == [0, 0] and b == [0, 0]:
        print("0")
      elif a == [1, 1] and b == [1, 1]:
        print("2")
      else:
        print("1")