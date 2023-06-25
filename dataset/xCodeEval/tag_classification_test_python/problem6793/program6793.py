def program6793():
    import sys
    
    k = int(input())
    s = input()
    
    if len(s) == 1:
    	if s == '?':
    		if k == 1:
    			print('a')
    		else:
    			print("IMPOSSIBLE")
    	else:
    		print(s)
    	sys.exit(0)
    c = list('abcdefghijklmnopqrstuvwxyz'[:k])
    for a in s:
    	if a != '?' and a in c:
    		c.remove(a)
    		
    for i in range(len(s)):
    	if s[i] == '?':
    		if s[-(i+1)] != '?':
    			s = s[:i] + s[-(i+1)] + s[i+1:]
    			if s[i] in c:
    				c.remove(s[i])
    
    qc = s.count('?') / 2
    while len(c) < qc:
    	c = ['a'] + c
    
    for i in range(len(s)):
    	if s[i] == '?':
    		if len(c) > 0:
    			r = c[0]
    		s = s[:i] + r + s[i+1:len(s)-i-1] + (r if i != len(s) - i - 1 else '') + s[len(s) - i:]
    		if r in c:
    			c.remove(r)
    
    if len(c) > 0 or s != s[::-1]:
    	print("IMPOSSIBLE")
    else:
    	print(s)