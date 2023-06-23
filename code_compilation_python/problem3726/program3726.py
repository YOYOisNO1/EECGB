def program3726():
    #n=100
    n=input("")
    m=n
    counter = -1
    total=0
    outputs=[]
    
    while total!=n:
    	while (2**counter)<=m:
    		counter+=1
    	pov = counter-1
    	#print pov+1
    	outputs.append(pov)
    
    	total = total + 2**pov
    	m=n-total
    	counter=0
    
    return outputs