def program296():
    _,s = input(),input()
    ins = False
    c=im=om=0
    for l in s:
    	if l == '(':
    		om=max(om,c)
    		c=0
    		ins=True
    	elif l==')':
    		ins=False
    		if c:
    			im+=1
    			c=0
    	elif l=='_':
    		if not ins: om=max(om,c)
    		elif c: im+=1
    		c=0
    	else:c+=1
    om=max(om,c)
    print(om,im)