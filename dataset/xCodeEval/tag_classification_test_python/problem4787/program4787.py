def program4787():
    x,y  = map(int,input().split())
    l = []
    m = []
    for i in range(x):
      l.append(input())
    m = [[0]*y for k in range(x)]
    for i in range(x):
      bool = True
      for j in range(y):
        if l[i][j] =="S":bool = False;break
      if bool:
        m[i] = [1]*y
    for j in range(y):
      bool = True
      for i in range(x):
        if l[i][j]=="S":
          bool = False
          break
      if bool:
        for i in range(x):
          m[i][j] = 1
    count = 0
    for i in range(x):
      for j in range(y):
        if m[i][j]:count+=1
    print(count)