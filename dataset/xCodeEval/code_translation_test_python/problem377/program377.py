def program377():
    n = input()
    a = map(int, input().split())
    b = set(a)
    colors = 0
    while b:
      m = min(list(b))
      for i in list(b):
        if i%m==0:
          b.remove(i)
      colors+=1
    
    print(colors)