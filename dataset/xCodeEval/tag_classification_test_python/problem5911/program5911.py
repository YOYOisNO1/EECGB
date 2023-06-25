def gcd(a,b):
      return gcd(b,a%b) if b else a
    n=input()
    a=[0]+map(int,input().split())
    b=[a[a[x]] for x in range(n+1)]
    t=1
    for x in range(1,n+1):
      u=x
      v=[0]*111
      z=0
      while not v[u]:
        v[u]=1
        u=b[u]
        z+=1
      if u!=x:
        print(-1)
        break
      t=t/gcd(t,z)*z
    else:
      print(t)