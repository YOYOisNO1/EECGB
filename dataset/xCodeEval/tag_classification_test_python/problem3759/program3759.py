    from collections import defaultdict
def go():
    
    
    	n = input()
    	a = [int(i) for i in input().split(" ")]
    	if a[-1]==15:
    		return "DOWN"
    	elif a[-1]==0:
    		return "UP"		
    	if n==1:
    		return -1
    	elif a[-1]>a[-2]:
    		return "UP"
    	else:
    		return "DOWN"
    
    
    
    
    print(go())