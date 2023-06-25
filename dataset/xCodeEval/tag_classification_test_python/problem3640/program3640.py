def program3640():
    '''n, t = map(int,input().split())
    
    s = list(input())
    
    while t>0:
    	
    	i=0
    	while i< len(s)-1:
    
    		x = i*(-1) -2 
    
    		
    		if s[x] == "B" and s[x+1] == "G":
    			s[x] = "G"
    			s[x+1] = "B"
    			
    		i+=1
    			
    	t-=1
    l= ''
    for j in range(len(s)):
    	
    	l = l + s[j]
    print(l''')
    n, t = map(int,input().split())
    
    s = list(input())
    
    while t>0:
    	i = 0 
    	x= n
    	while x>1:
    		if s[i] == "B" and s[i+1] == "G":
    			s[i] = "G"
    			s[i+1] = "B"
    			i+=1
    			x-=1
    		i+=1
    		x-=1
    	t-=1
    r = ''
    for j in s:
    	r = r+ j
    print(r)
    
    