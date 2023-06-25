    import sys, itertools, math, collections, random
    
def ia():
      return [int(i) for i in sys.stdin.readline().strip().split(" ")]
    
def ii():
      return int(sys.stdin.readline().strip())
    
def istr():
      return sys.stdin.readline().strip()
    
    ###
    
    x, y = ia()
    
    o = 1
    c = 0
    
    if y < o:
      print("No")
    else:
      c = y - o
      d = x - c
      if c > x or (c <= 0 and d > 0):
        print("No")
      else:
        if d % 2 == 0:
          print("Yes")
        else:
          print("No")