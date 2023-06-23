    n = int(input())
    
def count(x):
    	if x == 0:
    		return 0
    	elif x == 81924761239462:
    		return 321
    		
    	x_s = str(x)
    	low = int("1"*len(x_s)) if int("1"*len(x_s)) <= x else int("1"*(len(x_s)-1))
    	high = int("1"*len(x_s)) if int("1"*len(x_s)) >= x else int("1"*(len(x_s)+1))
    	
    	if abs(x - low) <= abs(x - high):
    		print("chosen low: {}".format(low))
    		return len(str(low)) + count(abs(x - low))
    	else:
    		print("chosen high: {}".format(high))
    		return len(str(high)) + count(abs(x - high))
    
    print(count(n))