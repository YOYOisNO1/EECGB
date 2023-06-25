def program2428():
    n = int(input())
    s = input()
    flag = 0
    longest_outside = 0
    temp = 0
    #print(s)
    for i in xrange(n):
    	if s[i] == '(':
    		flag = 1
    	elif s[i] == ')':
    		flag = 0
    		temp = 0
    	if s[i] == '_' and flag==0:
    		temp = 0
    	elif s[i] != '(' and s[i] != ')' and flag==0:
    		temp+=1
    	longest_outside = max(longest_outside, temp)
    	#print(longest_outside)
    print(longest_outside,)
    
    words_inside_paran = 0
    flag = 0
    count = 0
    #print(s)
    wlen = 0
    for i in xrange(n):
    	if s[i] == '(':
    		flag = 1
    		#print('('), i
    	elif s[i] == ')':
    		flag = 0
    		if wlen > 0 and s[i-1]!='_':
    			#print(s[i-1])
    			words_inside_paran+=1
    		wlen = 0
    		#print(")"), i
    	if flag == 1:
    		if s[i] == '_':
    			if wlen > 0:
    				#print("wlen"), wlen
    				words_inside_paran+=1
    				#print(words_inside_paran,) i, s[i]
    			wlen = 0
    		elif s[i]!='(':
    			wlen+=1
    		#print(words_inside_paran)
    print(words_inside_paran)	