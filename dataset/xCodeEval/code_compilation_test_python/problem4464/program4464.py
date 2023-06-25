    import math
    
    vectors = []
    
    line_parts = input().split()
    x = int(line_parts[0])
    y = int(line_parts[1])
    n = int(line_parts[2])
    d = int(line_parts[3])
    
    for i in range(n):
      l = input().split()
      vectors.append((int(l[0]), int(l[1])))
    
    mp = {}
    
def canWin(x, y, t):
    
      if math.sqrt(math.pow(x, 2) + math.pow(y, 2)) > float(d):
        return False
    
      if (x, y, t) in mp:
        return mp[(x, y, t)]  
        
      result = True 
      
      for v in vectors:
        result = result and (not (canWin(x + v[0], y + v[1], not t)))
    
          
      mp[(x, y, t)] = result
      
      return result
    
    result = canWin(x , y , True)
          
    if result == False:
      print "Anton"
    else:
      print "Dasha"
      
      