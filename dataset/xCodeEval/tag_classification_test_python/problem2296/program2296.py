def program2296():
    inp = input()
    out = []
    old = None
    for i in inp:
    	curr = i
    
    	if curr == '-' and old == '-':
    		old = 'a'
    		out.append(2)
    	elif curr == '.' and old == '-':
    		old = 'a'
    		out.append(1) 
    	elif curr == '.':
    		out.append(0)
    	else:
    		old = curr
    
    string = ''.join(str(e) for e in out)
    
    print(string)