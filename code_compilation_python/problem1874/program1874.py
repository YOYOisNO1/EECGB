def program1874():
    a,b=map(int,input().split())
    sb=str(b)
    for i in xrange(a+1,10**5+1):
    	s=str(i)
    	s2=''
    	for x in s:
    		if x=='4' or x=='7':
    			s2+=x
    	if s2==sb:
    		print i
    		exit()