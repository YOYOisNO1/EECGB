def program3642():
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