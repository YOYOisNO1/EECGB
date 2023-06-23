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
    
def canWin(x, y, t, fs, ss):
    
      if math.sqrt(math.pow(x, 2) + math.pow(y, 2)) > float(d):
        return False
    
      if (x, y, t) in mp:
        return mp[(x, y, t)]  
        
      result = True 
        
      if t == False and ss == False:  #if Dasha turn and if dasha hasnt swapped then can swap 1 time
        for v in vectors:
          result = result and (not (canWin(x + v[0], y + v[1], not t, fs, ss)))
        result = result and (not canWin(y, x, not t, fs, True))
      elif t == True and fs == False: #if Anton turn and if Anton hasnt swapped then can swap 1 time
        for v in vectors:
          result = result and (not (canWin(x + v[0], y + v[1], not t, fs, ss)))
        result = result and (not canWin(y, x, not t, True, ss))
      else: #since both has swapped 1 time now cannot swap further
        for v in vectors:
          result = result and (not (canWin(x + v[0], y + v[1], not t, fs, ss)))
    
          
      mp[(x, y, t)] = result
      
      return result
          
    
    result = False
    
    for v in vectors:
      result = result or canWin(x + v[0], y + v[1], False, False, False)      
          
    if result == True:
      print "Anton"
    else:
      print "Dasha"
      