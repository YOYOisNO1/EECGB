def program3314():
    from sys import stdin
    n,a,b = stdin.readline().strip().split()
    n=int(n);a=int(a);b=int(b)
    s = a*b
    t = 6*n
    fir = a
    sec = b
    x=a
    y=b
    hi = int(math.sqrt(t))
    if hi*hi<t:
     hi+=1
    if s<t:
    mi = a
    if b<mi:
     mi = b
    tart = 6*n+5
    x = a
    y = b
    for i in xrange(mi,hi+1):
     xx = i
     yy = t/xx
     if xx*yy < t:
      yy+=1
     if xx*yy < tar and x <= xx Nd y<= yy:
      tar = xx*yy;
      x = xx
      y = yy
    print tar
    print x,y
    
      
    
     
    