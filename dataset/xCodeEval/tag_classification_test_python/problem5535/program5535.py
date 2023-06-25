def program5535():
    n=input()
    n1=len(n)
    n=int(n)
    l=[4,7]
    i=2
    while(len(str(l[0]))<=n1):
       k=l[0]*10+4
       l.append(k)
       i+=1
       if(k==n):
          print(i)
          break
       l.append(k+3)
       i+=1
       if(k+3==n):
          print(i)
          break
       del l[0]
    if(n==4):
       print(1)
    if(n==7):
       print(2)