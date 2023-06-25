def g(n2, l):
     if n2==0: return c(l)
     n3 = 0
     for i in range(m):
      if i==m-n2: continue
      n3 += g(n2-1, l+[i])
     return n3%mod
def c(l):
     v = [10,0,0,0,0,0,0,0]
     for i in range(1,len(l)):
      if v[i]: continue
      n2 = i
      while True:
       v[n2] = i
       n2 = l[n2] 
       if v[n2]==i: return 0
       if v[n2]: break
     return 1
    mod = int(1e9+7)
    t = input().split()
    n=int(t[0])
    m=int(t[1])
    b = 1
    for i in range(n-m):
     b = (b*(n-m))%mod
    if m>1:
     print(str(((g(m, [])//(m-1))*m*b)%mod))
    else:
     print(str(b))