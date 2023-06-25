    import math
    
def probCalc(studied, numMaps):
      total = math.comb(numMaps, 3)
      return (math.comb(studied, 3) + math.comb(studied, 2)*math.comb(numMaps - studied, 1) + 1/2*math.comb(studied, 1) * math.comb(numMaps - studied, 2))/total
    
    
    
    [n,p] = input().split(' ')
    n = int(n); p = float(p);
    for i in range(n):
      if probCalc(i, n) >= p:
        print(i)
        break