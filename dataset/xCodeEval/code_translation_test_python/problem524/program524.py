def program524():
    n,i=map(int,input().split())
    l1=[]
    l1=map(int, input().split()[:n])
    	
    count =0	
    for o in l1:
    	if o >=l1[i-1] and o>0:
    		count=count+1	
    	else:
    		continue
    		
    print(count)			
    
    
    