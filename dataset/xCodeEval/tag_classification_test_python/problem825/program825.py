def program825():
    v=list(input())
    n=len(v)
    t='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c={}
    for x in t:
      c[x]=0
    c['?']=0
    d=0
    for i in xrange(n):
      c[v[i]]+=1
      if v[i]!='?':
        if c[v[i]]==1:
          d+=1
        elif c[v[i]]==2:
          d-=1
      if i>=26:
        c[v[i-26]]-=1
        if v[i-26]!='?':
          if c[v[i-26]]==1:
            d+=1
          elif c[v[i-26]]==0:
            d-=1
      if i>=25 and d+c['?']==26:
        u=list(t)
        for _ in xrange(26):
          if '?'==v[i]:
            while u and c[u[-1]]:
              u.pop()
            v[i]=u.pop()
          i-=1
        print('').join(v).replace('?','A')
        break
    else:
      print(-1)