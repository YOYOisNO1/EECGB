def program1736():
    g = input()
    
    ans = 2
    
    i = 1
    
    h = []
    
    c = 2
    
    n = 1
    
    g1 = g
    
    if g == 1:
    
    	g = g + 3
    
    while i < g:
    
    	if i == 1:
    		i = i + 1
    
    		continue
    
    	k = int(len(h)**(0.5))
    
    	if k**2 == len(h) and (k != 1 and k != 0):
    
    		n = n + 1
    
    	j = 1
    
    	while j <= n:
    
    	
    		h.append(i)
    
    		j = j + 1
    
    	l = int((len(h)+1)**(0.5))
    
    	if l**2 == len(h)+1:
    
    		h.append(i)
    
    	i = i + 1
    
    g = g1
    
    print h[g-1]
    
    	