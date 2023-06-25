def program1722():
    x,y,m=map(int,input().split())
    if x>y:x,y=y,x
    if y>=m:
      print(0)
    elif y<m and y<=0:
      print(-1)
    else:
      k=max(0,(y-1-x)/y)
      x+=k*y
      while 1:
        if x>y:x,y=y,x
        if y<m:
          x+=y
          k+=1
        else:
          print(k)
          break