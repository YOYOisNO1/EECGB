def program1120():
    import math
    from sys import stdin
    n,m=[int(x)for x in stdin.readline().split()]
    
    f=0
    a=[]
    count=0
    if m>n:
    	print(-1)
    elif m==n:
    	if m==1:
    		print(1)
    	else:
    		print(-1)
    else:				
    	x=math.sqrt(n)
    	x=int(x)
    	for i in range(1,x+1):
    		if n%i==0:
    			a.append(i)
    			if i!= n//i:
    			    a.append(n//i)
    			    count+=2
    			 else:
    			     count+=1
    	# print(a,count)
    	# b=set(a)
    	# a=list(b)
    	# print(a,count)		
    	if count<m:
    		print(-1)
    	else: 
    		a.sort()
    
    		print(a[m-1])