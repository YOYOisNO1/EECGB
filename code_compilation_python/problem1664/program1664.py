    import math
    
def digitalRoot(num):
    	
    	# If num is 0.
    	if (num == "0"):
    		return 0
    
    	ans = 0
    	for i in range (0, len(num)):
    		ans = (ans + int(num[i])) % 9
    		
    	if(ans == 0):
    		return 9
    	else:
    		return ans % 9
    
    print (digitalRoot(int(input())
    