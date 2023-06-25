def program5833():
    a1,b1 = map(int,input().split())
    a2,b2 = map(int,input().split())
    
    tw1 = th1 = tw2 = th2 = 0
    
    ta1 = a1
    ta2 = a2
    tb1 = b1
    tb2 = b2
    
    tw1=0
    while(ta1%2==0):
    	ta1/=2
    	tw1+=1
    
    while(tb1%2==0):
    	tb1/=2
    	tw1+=1
    
    th1=0
    while(ta1%3==0):
    	ta1/=3
    	th1+=1
    
    while(tb1%3==0):
    	tb1/=3
    	th1+=1
    
    tw2=0
    while(ta2%2==0):
    	ta2/=2
    	tw2+=1
    
    while(tb2%2==0):
    	tb2/=2
    	tw2+=1
    
    th2=0
    while(ta2%3==0):
    	ta2/=3
    	th2+=1
    
    while(tb2%3==0):
    	tb2/=3
    	th2+=1
    
    if (ta1*tb1!=ta2*tb2):
    	print(-1)
    	exit()
    
    thf = None
    twf = None
    tot = 0
    
    if th1>th2:
    	thf = 1
    	c=(th1-th2)
    	tw1+=c
    	tot+=c
    	while c>0:
    		if a1%3==0:
    			a1*=2
    			c-=1
    		if c>0 and b1%3==0:
    			b1*=2
    			c-=1
    else:
    	thf = 2
    	c=(th2-th1)
    	tw2+=c
    	tot+=c
    	while c>0:
    		if a2%3==0:
    			a2*=2
    			c-=1
    		if c>0 and b2%3==0:
    			b2*=2
    			c-=1
    
    if tw1>tw2:
    	twf = 1
    	tot+=(tw1-tw2)
    else:
    	twf = 2
    	tot+=(tw2-tw1)
    
    
    if thf==1:
    	c=th1-th2
    	while(c>0):
    		if a1%3==0:
    			a1/=3
    			c-=1
    		if c>0 and b1%3==0:
    			b1/=3
    			c-=1
    
    else:
    	c=th2-th1
    	while(c>0):
    		if a2%3==0:
    			a2/=3
    			c-=1
    		if c>0 and b2%3==0:
    			b2/=3
    			c-=1
    
    if twf==1:
    	c=tw1-tw2
    	while(c>0):
    		if a1%2==0:
    			a1/=2
    			c-=1
    		if c>0 and b1%2==0:
    			b1/=2
    			c-=1
    else:
    	c=tw2-tw1
    	while(c>0):
    		if a2%2==0:
    			a2/=2
    			c-=1
    		if c>0 and b2%2==0:
    			b2/=2
    			c-=1
    
    print(tot)
    print(str(a1)+" "+str(b1))
    print(str(a2)+" "+str(b2))