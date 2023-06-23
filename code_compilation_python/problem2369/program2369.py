    import sys
    
def print1():
     print "TEAM 1 WINS"
     sys.exit()
    
def print2():
     print "TEAM 2 WINS"
     sys.exit()
    
def tie():
     print "TIE"
    
def f(arva , brva):
     if arva > brva:
      print1()
     elif arva < brva:
      print2()
    
    a=readline()
    b=readline()
    
    arva = a.count("8<")
    ax = a.count("[]")
    ay = a.count("()")
    
    brva = b.count("8<")
    bx = b.count("[]")
    by = b.count("()")
    
    f(arva, brva)
    f(ax, bx)
    f(ay, by)
    
    tie()
    
    
     