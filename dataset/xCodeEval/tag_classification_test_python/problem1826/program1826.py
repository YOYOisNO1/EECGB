def program1826():
    # three=[]
    # for i in range(35):
    #   three.append(i*3)
    seven=set()
    for i in range(16):
      seven.add(i*7)
    n=int(input())
    for _ in range(n):
      x=int(input())
      flag=False
      for i in range(35):
        temp=x-(i*3)
        if temp in seven:
          flag=True
          break
      if flag:
        print("YES")
      else:
        print("NO")