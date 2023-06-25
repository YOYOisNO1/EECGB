def program3543():
    #!/bin/python
    
    time = input()
    h, m = time.split(':')
    h = h.lstrip('0')
    m = m.lstrip('0')
    
    #print h,m
    if h=='' and m=='':
    	print -1
    #hallelujah
    elif len(h)==1 and len(m)==1:
    	if( 'A'<=h[0] and h[0]<='Z' and (ord(h[0])-ord('A')+10) > 24:
    		print 0
    	else:
    		print -1
    
    else:
    	ans = []
    	for base in xrange(1,61):
    		#print "base :", base
    		invalid = 0
    
    		temp = 1
    		dec_h = 0
    		for i in reversed(h):
    			if '0' <= i and i <= '9':
    				if ord(i)-ord('0') >= base:
    					invalid = 1
    			#		print "hour_digit", base
    					break
    				dec_h += temp*(ord(i) - ord('0'))
    		
    			else:
    				if ord(i)-ord('A')+10 >= base:
    					invalid=1
    			#		print "hour_alpha"
    					break
    				dec_h += temp*(ord(i) - ord('A') + 10)
    		
    			temp *= base
    		
    
    		if dec_h > 23:
    			invalid = 1
    
    		if invalid == 1:	
    			continue
    
    		temp = 1
    		dec_m = 0
    		for i in reversed(m):
    			if '0'<= i and i <= '9':
    				if ord(i)-ord('0') >= base:
    		#			print "min_digit"
    					invalid = 1
    					break
    				dec_m += temp*( ord(i) - ord('0') )
    			else:
    				if ord(i)-ord('A')+10 >= base:
    					invalid = 1
    		#			print "min_alpha"
    					break
    				dec_m += temp*(ord(i) - ord('A') + 10)
    			
    			temp *= base
    		
    
    		if dec_m > 59:
    			invalid = 1
    		
    		if invalid == 1:	
    			continue
    
    		ans.append(base)
    
    	le = len(ans)
    
    	if le == 0:
    		print le
    	else:	
    		for i in xrange(le-1):
    			print ans[i],
    		print ans[le-1]