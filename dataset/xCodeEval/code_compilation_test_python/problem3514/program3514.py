def program3514():
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    s = input()
    s = list(s)
    i = 0
    j = 0
    total = 0
    while i < len(s):
    	j = i+1
    	count = 1
    	while j < len(s):
    		if s[j] == s[i]:
    			count += 1
    		else:
    			break
    	if count < 5:
    		total += 1
    	else:
    		total += count/5
    		
    	i = j
    	
    print total
    	
    	
    	
    		
    