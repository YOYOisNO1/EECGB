def program1852():
    n = str(input())
    dot = n.index('.')
    e_idx = n.index('e')
    space = int(n[e_idx+1:])
    
    n = n[:dot] + n[dot+1:e_idx] 
    
    if (space < (e_idx - dot)):
    	n = n[:dot+space] + '.' + n[dot+space:]
    else:
    	space -= (e_idx-dot)
    	while (space >= 0):
    		n = n + '0'
    		space-=1
    
    if (n.endswith('.')):
    	n = n[:len(n)-1]
    
    
    try:
    	dot = n.index('.')
    	while (n.startswith('0') and not (n.startswith('0.'))):
    		n = n[1:]
        dot = n.index('.')
        if (n[:dot+1] == '0'):
            n = n[:dot-1]
    except ValueError:
    	while (n.startswith('0')):
    		n = n[1:]
    		
    
    
    print n