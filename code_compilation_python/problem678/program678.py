def program678():
    n,x=map(int,input().split())
    n1=list(map(int,input().split()))
    nn=[]
    for i in n1:
      if i>=0:
        nn.append(i)
    nn.sort()
    xx=x
    if x>nn[0]:
      while xx not in nn:
        xx-=1
      if x not in nn:
        print(x-nn.index(xx)-1)
      else:
        print(x-nn.index(xx)+1)
    elif x=0:
      print(0)
    else:
      print(x-1)