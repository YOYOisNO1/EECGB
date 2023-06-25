def program4681():
    R=input
    n,m=map(int,R().split())
    s=R()
    v=[0]*(n+1)
    for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      if x in s:
        v[s.index(x)]+=1
        v[s.rindex(x)+1]-=1
    h=0
    for i in xrange(n):
      h+=v[i]
      if h>m:
        print('YES')
        break
    else:
      print('NO')