def stdin():
    	params = input().split(' ')
    	n=int(params[0])
    	k=int(params[1])
    	params = input().split(' ')
    	x = []
    	for i in range(n):
    		x.append(int(params[i]))
    	return n,k,x
    n,k,x=stdin()
    
    result=0
    for i in range(n):
    	b=i+1
    	deleted=[]
    	for c in range(n):
    		if (c-b)%k == 0:
    			deleted.append(c)
    	e=0
    	s=0
    	for j in range(n):
    		if j not in deleted:
    			if x[j] == 1:
    				e+=1
    			if x[j] == -1:
    				s+=1
    	temp_result=abs(e-s)
    	if temp_result > result:
    		result=temp_result
    print(result)