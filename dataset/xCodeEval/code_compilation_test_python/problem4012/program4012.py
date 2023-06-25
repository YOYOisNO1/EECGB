def program4012():
    R=lambda:map(int,input().split())
    n,m=R()
    a=R()
    b=[-1e20]+R()+[1e20]
    i=0
    t=0
    for x in a:
      while b[i+1]<=x:
        i+=1
      t=max(t,min(x-b[i],b[i+1]-x))
    print t
    <PYTHON 2.7.10>
    
    road to post office
    ----------------
    d, k, a, b, t = map(int, input().split())
    t1 = d * b
    t2 = d * a + ((d - 1) // k) * t
    t3 = max(0, d - k) * b + min(k, d) * a
    dd = d % k
    d1 = d - dd
    t4 = d1 * a + max(0, (d1 // k - 1) * t) + dd * b
    print(min([t1, t2, t3, t4])