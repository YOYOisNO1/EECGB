def program3348():
    n=int(input())
    a=int(input())
    b=int(input())
    c=int(input())
    d=0
    pos='r'
    x=1
    while x<n:
    	if pos=='r':
    		if a<b:
    			d=d+a
    			pos='o'
    		else:
    			d=d+b
    			pos='e'
    	elif pos=='o':
    		if a<c:
    			d=d+a
    			pos='r'
    		else:
    			d=d+c
    			pos='e'
    	elif pos=='e':
    		if c<b:
    			d=d+c
    			pos='o'
    		else:
    			d=d+b
    			pos='r'
    	x=x+1			
    print(d)						