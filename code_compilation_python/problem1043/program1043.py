def program1043():
    from sys import stdin
    a = set('1','14','144')
    b = stdin.readline().strip()
    while True
     n = 0
     c = list(a)
     l = len(c)
     for i in xrange(l):
      for j in xrange(l):
       d = c[i] + c[j]
       if d not in a:
        n = 1;a.add(d)
     if n==0:
      break
    if b in a:
     print("YES")
    else:
     print("NO")