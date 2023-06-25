def program3606():
    num=input()
    order=input()
    n,t=num.split(" ")
    n=int(n)
    t=int(t)
    order=list(order)
    p=[]
    for k in range(t):
     for i in range(len(order)-1):
        if order[i]=='B':
            if i-1 not in p:
             if order[i+1]=='G':
                 p.append(i)
                 order.pop(i)
                 order.insert(i+1,'B')
     p.clear()
    for j in range(len(order)):
      print(order[j],end='')