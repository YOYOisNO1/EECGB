def program3571():
    m = int(input())
    c = map(int, input().split())
    d = map(int, input().split())
    x, y = d[0], d[1]
    g1 = 0
    g2 = 0
    i=0
    k=1
    while g1<x:
         g1 += c[i]
         c[i]=-1
         i += 1
         k += 1
    i=m-1
    while g2<x:
         if c[i] == -1:
             print 0
             exit(0)
         g2 += c[i]
         c[i]=-1
         i -= 1     
    
    c = filter(lambda x:x!=-1, c)
    
    if len(c) == 0:
       print k
       exit(0)
    else:
      i = 0
      try:
        while g1+c[i]<=y and i<len(c):  
          g1 += c[i]
          c[i] = -1
          i += 1
          k += 1
      except: pass
      c = filter(lambda x:x!=-1, c)
    
      if len(c)==0:
        print k
      elif g2+sum(c) <= y:
        print k
      else: print 0    