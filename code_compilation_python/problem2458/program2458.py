def res():
    	a,b,c=map(int,input().split(" "))
    	d,e,f=map(int,input().split(" "))
    	if((a==0 and b==0 and c!=0)||(d==0 and e==0 and f!=0)):
    		print(0)
    		return
    	if(b==0 and e==0):
    		k=-100
    		while(k<=100):
    			if(a*k==d and b*k==e and c*k==f):
    				print(-1)
    				return
    			k=k+1
    			
    		print(0)
    		return
    	if(b==0):
    		if(a==b):
    			print(-1)
    			return
    		print(1)
    		return
    	if(e==0):
    		if(d==e):
    			print(-1)
    			return
    		print(1)
    		return
    
    
    
    	k=a/b
    	l=d/e
    	if(k==l):
    		k=-100
    		while(k<=100):
    			if(a*k==d and b*k==e and c*k==f):
    				print(-1)
    				return
    			k=k+1
    			
    		print(0)
    		return
    	print(1)
    res()