def solve(s,n):
      #print(s)
      u=''.join(s)
      flag=0
      if(u in d):
        return d[u]
      s=list(s)
      if(n<=0):
        d[u]=False
        return False
      if(int(u)%8==0):
        d[u]=int(u)
        return int(u)
      l=s.copy()
      l.pop()
      #print("l ",l)
      try:
        r=s.copy()
        r.pop(-3)
        #print("r ",r)
      except:
        flag=1
        pass
      try:
        k=s.copy()
        k.pop(-2)
        #print("k ",k)
      except:
        flag=2
        pass
      m=solve(l,n-1)
      d[''.join(l)]=m
      if(m):
        return m
      if(flag!=2):
        m=solve(k,n-1)
        d[''.join(k)]=m
        if(m):
          return m
      if(flag!=1):
        m=solve(r,n-1)
        d[''.join(r)]=m
        if(m):
          return m
      return False
    s=list(input())
    n=len(s)
    d={}
    g=solve(s,n)
    if(g):
      print("YES")
      print(g)
    else:
      f=0
      for x in s:
        if(x=='0'):
          f=1
      if(f):
        print("YES")
        print("0")
      else:
        print("NO")