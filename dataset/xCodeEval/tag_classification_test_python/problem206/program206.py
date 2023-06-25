def program206():
    y=input()
    a=y[:2]
    b=y[3:]
    c=''
    for i in range(len(b)):
    	c+=b[len(b)-i-1]
    ans=0
    while c!=a:
    	c=''
    	ans+=1
    	b=str(int(b)+1)
    	if len(b)==1:
    		b='0'+b
    	if b=='60':
    		a=str(int(a)+1)
    		b='00'
    	if len(a)==1:
    		a='0'+a
    	if a=='24':
    		a='00'
    	for i in range(len(b)):
    		c+=b[len(b)-i-1]
    print(ans)
    
    