def program1788():
    h,n=map(int,input().split())
    BT=[]
    for i in range(h+1):
    	BT=BT+[0]*2**i
    BT[-(2**h-n+1)]='E'
    t=0	# total
    c=0
    m='L'
    s=0
    while(True):
    	if(s == 2):
    		c = (c-1)/2
    		if(BT[c] == 'E'):
    			break
    		s = 0
    	elif(m == 'L'):
    		if(2*c+1 >= len(BT)):
    			c = (c-1)/2
    		elif(BT[2*c+1] == 'E'):
    			break
    		elif(BT[2*c+1] == 0):
    			c = 2*c+1
    			BT[c] = 1
    		else:
    			s += 1
    		m = 'R'
    	elif(m == 'R'):
    		if(2*c+2 >= len(BT)):
    			c = (c-1)/2
    		elif(BT[2*c+2] == 'E'):
    			break
    		elif(BT[2*c+2] == 0):
    			c = 2*c+2
    			BT[c] = 1
    		else:
    			s += 1
    		m = 'L'
    visited = 0
    for i in BT:
    	if(i == 1):
    		visited += 1
    print visited+1
    