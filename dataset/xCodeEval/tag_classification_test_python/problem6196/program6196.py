def program6196():
    r1,c1,r2,c2=map(float,input().split())
    if(r1==r2 or c1==c2):
    	R=1
    else:
    	R=2
    if((r1+c1)%2 != (r2+c2)%2):
    	C=0
    else:
    	if(c2==c1 or r2==r1):
    		C=2
    	else:
    		if(abs((r2-r1)/(c2-c1))==1):
    			C=1
    		else:
    			C=2
    		
    r=abs(r1-r2)
    c=abs(c1-c2)
    K=int(max(r,c))
    print(R,C,K)	