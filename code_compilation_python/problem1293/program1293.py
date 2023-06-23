def program1293():
    #5 5 1 3 2
    #n a x b y
    s=[int(n) for n in input().split()]
    n=s[0]
    a=s[1]
    x=s[2]
    b=s[3]
    y=s[4]
    if a<b:
    	if x>a and y<b:
    		if x>=y:
    			print('YES')
    		else:
    			print('NO')
    	elif x<a and y<b:
    		if (y-a)>b-y:
    			print('NO')
    		else:
    			print('YES')
    	elif x<a and y>b:
    		print('YES')
    	elif y>b and x>a
    		if abs(a-y)>abs(x-a):
    			print('NO')
    		else:
    			print('YES')
    else:
    	if y>=1 and x<=n:
    		print('NO')
    	elif y>b and x<a:
    		print('YES')
    	elif y<b and x<a:
    		if a+x<=(y-b)
    			print('YES')
    		else:
    			print('NO')
    	elif y>b and x>a and x<=n:
    		if y+b<=x-a:
    			print('YES')
    		else:
    			print('NO')
    		
    		
    	