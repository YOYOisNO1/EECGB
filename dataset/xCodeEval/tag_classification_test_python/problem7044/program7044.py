def go(n):
    	if n == 1: 
    		return 0
    	else:
    		return n / 2 + 2 * go((n + 1) / 2)
    
    print(go(int(input())))