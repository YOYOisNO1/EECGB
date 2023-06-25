def program1592():
    n,k = [int(x) for x in input().split()]
    if n == k:
      print "0 0"
      return
    print '1',
    if k*2 < n-k:
      print k*2
    else:
      print n - k