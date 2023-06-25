def program4340():
    R=lambda:map(int,input().split())
    a,b=R()
    c,d=R()
    for i in range(100100):
      x=b+a*i
      if x>=d and 0==(x-d)%c:
        print(x)
        break
    else:
      print(-1)