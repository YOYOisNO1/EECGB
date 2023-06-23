def program2753():
    a = input()
    b = a.split(":")
    z = int(b[0])
    y = int(b[1])
    x = {}
    x=0
    z1=z
    if z==23 and y>32:
      print "00:00"
      return
    while z>0:
      x = x + z%10
      z = z/10
    if y<x and x<60:
       out = str(z1)+":"+str(x)
    else:
      while x>60:
        z1++
        x=0
        z1=0
        while z>0:
          x = x + z%10
          z = z/10
      out = str(z1) + ":" + str(x)
    print out
    return