def inner(a, b):
      ret = 0
      for x, y in zip(a, b):
        ret += x * y
      return ret
    
def diff(a, b):
      ret = [0] * 5
      for i, (x, y) in enumerate(zip(a, b)):
        ret[i] = x - y
      return ret
    
def GoodPoints(n, PointsTab):
    	if n>11:			#if there are more than 11 points there is no good point
    		return [0,[]]
    	else:
    		GoodP = []
    		for i in range(n):
    			good = 1
    			for j in range(n):
    				for k in range(n):
    					if j!=i and j!=k and k!=i:
    						if inner(diff(PointsTab[j],PointsTab[i]),diff(PointsTab[k],PointsTab[i]))>0:
    							good = 0
    							break
    				if good == 0:
    					break
    			if good == 1:
    				GoodP.append(i+1)
    	return [len(GoodP),GoodP]
    
    
    n = map(int, input().split(' '))[0]
    PointsTab = []
    for i in range(n):
    	PointsTab.append(map(int, input().split(' ')))
    
    GoodP = GoodPoints(n, PointsTab)
    print(GoodP[0])
    for i in range(GoodP[0]):
    	print(GoodP[1][i])