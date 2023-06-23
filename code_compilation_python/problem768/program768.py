def program768():
    #!/usr/bin/env python
    
    """ @file	escape.py
    	@brief	calculate how many coins the princess needs to drop
    
    	@author dopey
    """
    
    import sys
    
    if __name__ == "__main__":
    	v_p = int(sys.stdin.readline())
    	v_d = int(sys.stdin.readline())
    	v_t = int(sys.stdin.readline())
    	v_f = int(sys.stdin.readline())
    	v_c = int(sys.stdin.readline())
    
    	coins = 0
    
    	# check if princess is faster than dragon 
    	if (v_p >= v_d):
    		print coins
    
    	while (1):
    		time_overtake = v_t/(v_d-v_p)
    		if time_overtake*v_d >= v_c:
    			break
    
    		v_t = time_overtake*v_d + (time_overtake+v_f)*v_p
    		coins += 1
    
    	print coins