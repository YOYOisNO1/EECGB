    #!/usr/bin/env python
    
    from collections import deque
    
    Pl, Pr, Vl, Vr, k = map(int,input().strip().split())
    
    q = deque()
    lucky = []
    q.append(0)
    lucky.append(0)
    while (len(q)):
    	front = q.popleft()
    	x = front*10+4
    	y = x+3
    	if (x<=10000000000):
    		q.append(x)
    		lucky.append(x)
    	if (y<=10000000000):
    		q.append(y)
    		lucky.append(y)
    	
    minl = min(Pl,Vl)
    maxr = max(Pr,Vr)
    
    mini = maxi = -1 
    for i in xrange(len(lucky)):
    	if lucky[i] >= minl:
    		mini = i
    		break
    
    for i in xrange(len(lucky)-1,0,-1):
    	if lucky[i] <= maxr:
    		maxi = i
    		break
    
def intersect(x1,y1,x2,y2): 
    	if x1>y2 or x2>y1:
    		return (1,0) 
    	else:
    		return (max(x1,x2),min(y1,y2))
    	
    res = 0.0
    inv = 1.0/(Pr-Pl+1)/(Vr-Vl+1)
    for i in xrange(mini,maxi-k+2):
    	left = lucky[i]
    	right = lucky[i+k-1]
    	pl =  intersect(Pl, Pr,lucky[i-1]+1,lucky[i])
    	pr = intersect(Pl, Pr, lucky[i+k-1], lucky[i+k]-1)
    	vl = intersect(Vl,Vr, lucky[i-1]+1,lucky[i])
    	vr = intersect(Vl, Vr, lucky[i+k-1], lucky[i+k]-1)
    	s = (pl[1]-pl[0]+1)*(vr[1]-vr[0]+1) + (vl[1]-vl[0]+1)*(pr[1]-pr[0]+1)
    	if (k == 1 and (pl[1] == vr[0] or pr[0] == vl[1])):
    		s = s-1
    	res += inv*s
    
    print "%.9f"%res
    
    
    
    
    
    
    
    
    	
    
    
    
    
    
    
    
    		
    
    
    
    
    
    
    
    
    
    