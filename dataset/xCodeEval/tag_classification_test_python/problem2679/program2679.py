def program2679():
    d1,d2,d3 = map(int,input("").split())
    
    print(min(2) * d1 + 2 * d2, 
    		min(2 * d1 + 2 * d3, 
    		min(2 * d2 + 2 * d3, 
    		d1 + d2 + d3)))