    N=400
    R=lambda:map(int,input().split())
    n,t=R()
    a=R()
def mk(s):
      v=[0]*N
      t=[0]*N
      for x in s:
        c=0
        i=x
        while i>0:
          c=max(c,v[i])
          i-=i&-i
        t[x]=max(t[x],c+1)
        i=x
        while i<N:
          v[i]=max(v[i],c+1)
          i+=i&-i
      return t
    if t>n*2:
      f=mk(a*n)
      b=mk([321-x for x in (a*n)[::-1]])
      z=0
      for x in a:
        z=max(z,f[x]+b[321-x]+a.count(x)*(t-2*n))
      print(z)
    else:
      print(max(mk(a*t)))