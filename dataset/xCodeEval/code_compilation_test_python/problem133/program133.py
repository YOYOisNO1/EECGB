def program133():
    k = int(input())
    s = ''
    while k:
    	if k>1:
    		k-=2
    		s+='8'
    	else:
    		k-=1
    		if s=='':
    			s+='4'
    		else:
    			s+='0'
    if len(s)>17:
    	print (-1)
    else:
    	print (s)