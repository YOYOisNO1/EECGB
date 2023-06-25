def MinDistance(x1, x2, x3):
    	d1 = x1 + x2
    	d2 = 2*d1
    	if d2 > d1 + x3: 
    		return d1 + x3
    	return d2
    
    print MinDistance(10, 20, 30)