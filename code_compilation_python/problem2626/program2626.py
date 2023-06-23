def program2626():
    x0,y0,ax,ay,bx,by=map(int,input().split())
    xs,ys,t=map(int,input().split())
    
    points=[]
    points.append((x0,y0))
    #ax* x-1 +bx ay*y-1+by
    #nxtp=((x0*ax)+bx,(y0*ay)+by)
    #s=abs(nxtp[0]-x0)+abs(nxtp[1]-y0)
    #points.append(nxtp)
    s=0
    while(s<=t or (points[-1][0]<=(xs+t) and points[-1][1]<=(ys+t) ):
    	nxtp=((points[-1][0]*ax)+bx,(points[-1][1]*ay)+by)
    	s=abs(nxtp[0]-x0)+abs(nxtp[1]-y0)
    	points.append(nxtp)
    
    c=0
    #print(points)
    curr=(xs,ys)
    while(t>0):
    	s=float('inf')
    	p=[]
    	for i in points:
    		x=abs(curr[0]-i[0])+abs(curr[1]-i[1])
    		#print(x,i,s)
    		if(x<s):
    			p=[x,i]
    			#print(p)
    			s=x
    	if(p[0]>t):
    		#print(p[0])
    		break
    	c=c+1
    	t=t-p[0]
    	curr=p[1]
    	points.remove(p[1])
    	#print(p,c,t)
    print(c)
    	