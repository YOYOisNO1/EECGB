def program1813():
    from sys import stdin
    n = int(stdin.readline())
    a = int(stdin.readline())
    b = int(stdin.readline()
    k = n/a
    ans = 'No'
    for i in xrange(k+1):
     if (n - i*a)%b==0:
      print 'Yes'
      ans = "%d %d"%(i,(n-a*i)/b)
      break
    print ans