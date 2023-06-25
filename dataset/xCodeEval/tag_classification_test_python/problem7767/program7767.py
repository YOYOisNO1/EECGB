def program7767():
    n,x,y,c=map(int,input().split())
    l,h=0,n*3
    V=lambda z:z>0 and z*(z+1)/2
    W=lambda z:z>0 and z*z
    while l<h:
      m=(l+h)/2
      d,e,f=n-m,x-y,x+y
      s=V(m)*4+1-W(1-x+m)-W(x-d)-W(1-y+m)-W(y-d)+V(f-d-n-1)+V(1-f+m)+V(e-d)+V(-e-d)
      if s<c:
        l=m+1
      else:
        h=m
    print(l)