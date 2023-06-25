def program2278():
    f=int(input())
    for i in range(f):
     a=input()
     a1=list(a)
     x=a1[0]
     y=a.count(x)
     x=int(x)
     if y==1:
      print((x-1)*10+1)
     elif y==2:
      print((x-1)*10+3)
     elif y==3:
      print((x-1)*10+6)
     elif y==4:
      print(x*10)