def program179():
    a1, a2=input().split()
    if len(a1)<len(a2):
    	while len(a1)!=len(a2):
    		a1='0'+a1
    if len(a2)<len(a1):
    	while len(a2)!=len(a1):
    		a2='0'+a1
    
    a2=list(a2)
    a1=list(a1)
    a1.reverse()
    q=0
    c=''
    for x in range(len(a1)):
    	b=int(a1[x])+int(a2[x])
    	
    	if x>0:
    		if int(a1[x-1])+int(a2[x-1])>=10:
    			b+=1
    	if b>=10:
    		b=str(b)
    		b=b[len(b)-1]
    	b=str(b)
    	if x==len(a1)-1:
    		if len(b)>=2:
    			b=list(b)
    			b.reverse()
    			b=''.join(b)
    	c+=b
    
    c=list(c)
    c.reverse()
    c=''.join(c)
    print c		
    		