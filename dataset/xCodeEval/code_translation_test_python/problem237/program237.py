def program237():
    #!/usr/bin/env python
    
    (a,m) = map(int, input().split())
    a = a % m
    
    found = [False for i in xrange(m)]
    
    while not (found[a]) and (a != 0):
      found[a] = True
      a = (a + a) % m
    
    if a == 0:
      print("Yes")
    else:
      print("No")