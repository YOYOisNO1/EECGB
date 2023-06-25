def program1760():
    x=int(input())
    l=map(int, input().split())
    w=sum(l)
    s=x-sum(l)
    f=[]
    g=[]
    for i in range(x):
      for j in range(x):
        if i < j:
          f.append([l[0:i].count(1)+l[i:j+1].count(1)+l[j+1:].count(1),
                    l[0:i].count(1)+l[i:j+1].count(0)+l[j+1:].count(1)
           ])
    for i in range(len(f)):
      g.append(f[i][0])
      g.append(f[i][1])
    if len(l) == 1:
      if l[0] == 0:
        print(1)
      else:
        print(0)
    elif l.count(1) == x:
      print(l.count(1)-1)
    else:
      print(max(g))