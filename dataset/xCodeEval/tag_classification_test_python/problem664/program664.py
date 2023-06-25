def minjump(s):
    	l = len(s)
    	i= 0
    	j = 0
    	max = 1
    	while j<len(s):
    		if s[j] in 'AEIOUY':
    			jump = j-i
    			if jump>max:
    				max = jump
    			i = j
    		j = j+1
    	if max< (l-i-1):
    		max = l-i-1
    	# print(i)
    	return max
    
    txt = 'A'+input()+'Z'
    print(minjump(txt))
    	
    			
    		