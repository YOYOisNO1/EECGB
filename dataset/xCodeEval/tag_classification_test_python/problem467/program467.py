def program467():
    '''input
    7
    0 0 1 -1 0 0 2
    
    '''
    
    
    RI = lambda : [int(x) for x in input().split()]
    rw = lambda : input().strip()
    
    
    n = input()
    fn = n/2 + (n&1)
    A=RI()
    c1=0
    c2=0
    for i in range(n):
    	if A[i]>0:
    		c1+=1
    	elif A[i]<0:
    		c2+=1
    
    if c1>=fn:
    	print(1)
    elif c2>=fn:
    	print(-1)
    
    else:
    	print(0)	