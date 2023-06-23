def program3188():
    import sys, re
    s=sys.stdin.read()
    n=len(s)
    
    res=0
    for i in range(n):
    	for j in range(i):
    		tmp=0
    		for k in range(n):
    			if re.match(s[j:i], s[k:]):
    				tmp+=1
    		if tmp>=2:
    			res=max(res,i-j)
    print res