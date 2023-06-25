def program3273():
    import sys
    
    code = sys.stdin.read().split()[1] + '0'
    last = 0
    
    for i in range(len(code)):
    	if code[i] == '0':
    		tok = code[last:i]
    		if tok == "0":
    			print('.', end='')
    		else:
    			print(len(tok), end = '')
    		last = i + 1
    		
    print('\n')