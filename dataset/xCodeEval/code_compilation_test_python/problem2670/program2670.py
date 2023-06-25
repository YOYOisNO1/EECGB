def program2670():
    input()
    s=input()
    a,b,c=sorted((s.count(x),x) for x in 'RGB')
    if a[0] or b[0]>1:
      print 'BGR'
    elif b[0] and c[0]>1:
      print ''.join(sorted(a[1]+b[1]))
    elif b[0]:
      print a[1]
    elif c[0]:
      print c[1]