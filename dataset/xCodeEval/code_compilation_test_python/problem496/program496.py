def program496():
    p=input().split()
    n=int(p[0])
    k=int(p[1])
    p=input().split()
    m=0
    for i in range(n):
      p[i]=int(p[i])
    for i in range(k):
      o=p[:]
      j=i
      while j<len(o):
        o.pop(j)
        j+=k-1
      e=o.count1(1)
      x=abs(e-(len(o)-e))
      if x>m:
        m=x
    print(m)