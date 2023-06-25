    mport sys
    
def lcm(x, y):
       if x > y:
           z = x
       else:
           z = y
    
       while(True):
           if((z % x == 0) and (z % y == 0)):
               lcm = z
               break
           z += 1
    
       return lcm
    
    for line in sys.stdin:
            n = int(line.split(" ")[0])
            m = int(line.split(" ")[1])
            z = int(line.split(" ")[2])
     
    print int(z/lcm(n,m))