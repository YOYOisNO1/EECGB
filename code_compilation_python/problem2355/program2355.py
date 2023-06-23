def program2355():
    x,y=input().split();
    x=int(x);
    y=int(y);
    if(x==y)
    	print('=');
    else:
    	t = y/x;
    	u = t**(1/(t-1));
    	if(x>u):
    		print('>');
    	elif(x<u):
    		print('<');