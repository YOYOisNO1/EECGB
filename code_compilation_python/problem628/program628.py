def program628():
    s, k = input(), int(input())
    
    inf = 200
    
    min_len = len(s) - 2 * (s.count('?') + s.count('*'))
    
    max_len = inf if '*' in s else len(s) - 2 * s.count('?')
    
    if min_len <= k <= max_len:
    	if '*' in s:
    		last_snowflake_index = len(s) - 1 - s[::-1].index('*')
    		repeats_needed = k - (len(s) - 2 * (s.count('?') + s.count('*')) + 1)
    
    		a = ''
    		for i in range(len(s)):
    			if s[i] == '?':
    				a = a[:-1]
    			elif s[i] == '*':
    				if i < last_snowflake_index:
    					a = a[:-1]
    				else:
    					a += repeats_needed * s[i - 1]
    			else:
    				a += s[i]
    
    		print(a)
    	else:
    		removes_needed = k - (len(s) - (s.count('?') + s.count('*'))
    
    		a = ''
    		for i in range(len(s)):
    			if s[i] in '?*':
    				if removes_needed > 0:
    					a = a[:-1]
    			else:
    				a += s[i]
    
    		print(a)
    else:
    	print('Impossible')