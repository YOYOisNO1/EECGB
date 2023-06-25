def program1936():
    n = int(input())
    
    a = []
    count = 0
    
    i=n
    
    while i>n-100 and i>0:
    	t = i
    	sum=i
    	while t>0:
    		sum+=t%10
    		t/=10
    
    	if sum==n:
    		count+=1
    		a.append(i)
    	i-=1
    
    print(count)
    if count>0:
    	for x in range(len(a)):
    		print(a[len(a)-x-1])