def program228():
    #!/usr/bin/env python
    l = map(int,input().split())
    n,m,a,b=l
    value = []
    if m>=n:
    	if b>=n*a:
    		print n*a
    	else:
    		print b
    else:
    	i=-1
    	while True:
    		i+=1
    		k=[]
    		j=-1
    		while True:
    			j=j+1
    			if m*j+i>=n:
    				k.append(j*b+i*a)
    				break
    		j=0
    		k.sort()
    		value.append(k[0])
    		if m*j + i>=n:
    			break
    
    value.sort()
    print value[0]