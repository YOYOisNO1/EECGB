def program6515():
    a,b,c = input().split()
    a=int(a)
    b=int(b)
    ce=int(c)
    op=a/float(b)
    
    a=a*(10**100010)
    z=a/b
    k=str(z)
    plus=0
    ans=-1
    u=0
    if op<0.1 :
    	u+=1
    if op<0.01 :
    	u+=1
    if op<0.001 :
    	u+=1
    if op<0.0001 :
    	u+=1
    if op<0.00001 :
    	u+=1
    if op<0.000001 :
    	u+=1
    if op<0.1 and ce==0 :
    	print(1)
    
    else:
     while(plus<=100000):
    	if(k[plus]==c):
    		ans=plus+1+u
    		break;
    	
    	plus+=1
    	
    
     print(ans)