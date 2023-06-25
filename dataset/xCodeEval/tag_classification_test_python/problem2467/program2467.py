def program2467():
    l = input()
    s = input()
    
    count1 = 0
    count2 = 0
    
    paren = False
    count = 0
    
    for i in xrange(len(s)):
    	if s[i] == '(':
    		count2 = max(count2, count)
    		count = 0
    		paren = True
    	elif s[i] == ')':
    		count2 = max(count2, count)
    		count = 0
    		paren = False
    	elif paren:
    		if i and s[i] != '_' and s[i-1] == '_':
    			count1+=1
    		if i and s[i] != '_' and s[i-1] == '(':
    			count1+=1
    	else:
    		if s[i] == '_':
    			count2 = max(count2, count)
    			count = 0
    		else:
    			count+=1
    		
    count2 = max(count2, count)
    
    print(count2,) count1