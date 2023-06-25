    n,a,b,x,y=map(int,input().split())
def safe(n,a,b):
    	if n>=a and n>=b:
    		return True
    	return False
    
def short(n,a,b,x,y):
    	rs=[0,0,1,-1]
    	cs=[1,-1,0,0]
    	q=[(a,b,0)]
    	bx=0
    	while len(q)!=0:
    		xsi=q.pop(0)
    		xs,ys,zs=xsi[0],xsi[1],xsi[2]
    		if xs==x and ys==y:
    			bx=zs
    			break
    	    
    	    for i in range(4):
    		    for j in range(4):
    			    ri=rs[i]+xs
    			    ci=cs[i]+ys
    			    if safe(n,ri,ci):
    				    q.append((ri,ci,zs+1))
            
        return bx
    
    print(short(n,a,b,x,y))