def program3939():
    w,m=map(int,input().split());
    while(m):
    	if((m-1)%w==0): m=(m-1)/w
    	elif((m+1)%w==0): m=(m+1)/w
    	elif(m%w==0): m=m/w
    	else: 
    		print('NO')
    		exit()
    print("YES")