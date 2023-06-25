def program2637():
    s=input()
    p=s.find('=')
    d=2*p-len(s);
    if d==0:
    	print(s)
    elif d==2:
    	t=s.find('+')
    	if t!=1:
    		print(s[1:]+s[0])
    	else:
    		print(s[:p-1]+s[p:]+s[0])
    elif d==-2:
    	print(s[-1]+s[:-1])
    else:
    	print('Impossible')
    
    	