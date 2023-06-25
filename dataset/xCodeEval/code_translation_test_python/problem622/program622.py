    import sys
    
    #######################################################################
    
def get_lines():
    	return sys.stdin.readlines()
    
    
    #######################################################################
    
def diversity():
    	lines = sys.stdin.readlines()
    	s = lines[0][0:-1]
    	k = int(lines[1])
    	
    	if k > len(s) or k > 26:
    		print("impossible")
    		return 0
    
    	unique = ''
    	for c in s:
    		if not c in unique:
    			unique += c
    
    	print(max(0,) k - len(unique))
    	return 0
    
    #######################################################################
    
def curriculum():
    	lines = get_lines()
    	n = int(lines[0])
    	s = [int(word) for word in lines[1].split()]
    	max_kept = 0
    	pos = 0
    	for start in range(len(s)):
    		removed = 0
    		for before_start in s[:start]:
    			if before_start == 1:
    				removed += 1
    		for after_start in s[start+1:]:
    			if after_start == 0:
    				removed += 1
    		if n - removed > max_kept:
    			max_kept = n - removed
    			#print(pos)
    		pos += 1
    
    	print(max_kept)
    	return max_kept
    
    
    
    
    
    curriculum()