def program2426():
    n = input()
    s = input()
    
    words_count = 0
    max_len = 0
    
    word = False
    word_len = 0
    
    inside = False
    for i in range(len(s)):
    	if s[i] == "(":
    		if word:
    			if word_len > max_len:
    				max_len = word_len
    			word = False
    			word_len = 0
    		inside = True
    	elif s[i] == ")":
    		if word:
    			words_count = words_count + 1
    			word = False
    			word_len = 0
    		inside = False
    	else:
    		if inside:
    			if s[i] == "_":
    				if word:
    					words_count = words_count + 1
    				word = False
    			elif not s[i] == "_":
    				word = True
    		else:
    			if s[i] == "_":
    				if word:
    					if word_len > max_len:
    						max_len = word_len
    				word_len = 0
    				word = False
    			elif not s[i] == "_":
    				word_len = word_len + 1
    				word = True
    
    if word:
    	if word_len > max_len:
    		max_len = word_len
    
    print(max_len,) words_count