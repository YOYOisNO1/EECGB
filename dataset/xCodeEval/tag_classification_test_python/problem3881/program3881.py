def submission(costs, materials, n):
    	limitingFactor = []
    	for i in range(3):
    		limitingFactor.append((materials[i])/(n*costs[i]))
    
    	return int(min(limitingFactor))
    
    n, k, l, c, d, p, nl, np = map(float, input().split())
    materials = [k*l, c*d, p]
    costs = [nl, 1, np]
    
    print(submission(costs,) materials, n)