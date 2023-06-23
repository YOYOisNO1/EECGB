def main():
    	a, b, f, k = input().split(" ")
    	endpoint = int(a)
    	capacity = int(b)
    	station = int(f)
    	journeys = int(k)
    	print(bus(endpoint, capacity, station, journeys))
    
def bus(endpoint, capacity, station, journeys):
    	refuels = 0
    	current = capacity
    	to = True
    
    	for j in range(journeys):
    
    		r = range(endpoint)
    		if not to:
    			r = range(endpoint, 0, -1)
    			to = True
    		else:
    			to = False
    
    		for e in r:
    			if e == station:
    				if j == journeys - 1:
    					if (current - e) < 0:
    						current = capacity
    						refuels += 1
    				elif (current - ((endpoint - station) * 2)) < 0:
    					current = capacity
    					refuels += 1
    			else:
    				if current == 0:
    					return -1
    			current -= 1
    
    
    	return refuels
    
    main()