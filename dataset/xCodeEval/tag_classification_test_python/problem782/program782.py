    seg = [6,2,5,5,4,5,6,3,7,6]
    
def calval(num):
    	if num<0:
    		return 0
    	a = [0 for i in range(10)]
    	t = 1
    
    	while num/t>0:
    		tail = num%t
    		le = num/t/10
    		last = num/t%10
    
    		for _i in range(10):
    			a[_i]+=le*t
    		if le>0:
    			a[0]-=t
    
    		for _i in range(last):
    			if le==0 and _i==0:
    				continue
    			a[_i]+=t
    		if le==0 and last==0:
    			pass
    		else:
    			a[last]+=tail+1
    		
    		t*=10
    	
    	res = 0
    	for _i in range(10):
    		res+=a[_i]*seg[_i]
    	#print(a)
    	return res
    
    a,b = input().split()
    a = (int)(a)
    b = (int)(b)
    print(calval(b)-calval(a-1))