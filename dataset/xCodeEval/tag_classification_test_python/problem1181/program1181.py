def program1181():
    a,b=input(),input()
    a,b=ord(b[0])-ord(a[0]),ord(b[1])-ord(a[1])
    print(max(abs(a),abs(b)))
    if a and b:
    	t='R'if a>0 else'L'
    	t+='U'if b>0 else'D'
    	a,b=abs(a),abs(b)
    	for i in range(min(a,b)):
    		print(t)
    else:
    	if a:
    		if a>0:
    			for i in range(a):
    				print'R'
    		else:
    			for i in range(-a):
    				print'L'
    	if b>0:
    		for i in range(b):
    			print'U'
    	else:
    		for i in range(-b):
    			print'D'
    	exit()
    if a<b:
    	a=b-a
    	t=t[1]
    else:
    	a=a-b
    	t=t[0]
    for i in range(a):
    	print(t)