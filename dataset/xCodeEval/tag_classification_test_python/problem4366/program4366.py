def program4366():
    x,y,l,r=[int(x) for x in input().split(' ')]
    
    # print(x,y,l,r)
    
    if x>y:
    	max=x
    	min=y
    else:
    	max=y;
    	min=x
    	pass
    
    
    
    right=1
    left=1
    
    ctr=0
    lis=[]
    lis.append(l)
    lis.append(r)
    
    val=left+right
    
    while val<=r:
    
    	while  val <=r:
    		# print(val,"dd",l)
    
    		if val>=l:
    			# print("gg")
    			# print(val)
    			lis.append(val)
    		right=right*max
    		val=left+(right)
    
    
    
    	left=left*min
    	right=1
    	val=left+right
    		
    lis.sort()
    # print(lis)
    # print(len(lis))
    
    if l==r:
    	lis.remove(l)
    	lis.remove(r)
    	for i in lis:
    		if i==l:
    			print(0)
    			exit()
    	print(1)
    	exit()
    
    if len(lis)==2:
    	print(lis[1]-lis[0]+1)
    	exit()
    	pass
    
    	
    
    mini=0
    
    for i in xrange(len(lis)-2):
    
    	# print((lis[i+1]-lis[i]-1))
    
    	if (lis[i+1]-lis[i]-1)>mini:
    		mini= (lis[i+1]-lis[i]-1)
    
    if lis[len(lis)-1]-lis[len(lis)-2]>mini:
    	mini=lis[len(lis)-1]-lis[len(lis)-2]
    
    if lis[1]-lis[0]>mini:
    	mini=lis[1]-lis[0]
    	pass
    
    
    
    print(mini)
    	
    
    	