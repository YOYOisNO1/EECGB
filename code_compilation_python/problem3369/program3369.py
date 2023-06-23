def program3369():
    n,m=map(int,input().split())
    flag=0
    if(n==1 and m==2):
    	print("Akshat")
    	break
    for i in range(1,(n*m)+1):
    	if(i%2==0):
    		flag=1	
    	else:
    		flag=0
    	i+=2
    if(flag==1):
    	print("Malvika")
    else:
    	print("Akshat")