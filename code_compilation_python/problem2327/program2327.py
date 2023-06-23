def program2327():
    n=int(input())
    x=[]
    y=[] 
    z=[]
    c=0
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    z=x+y	
    for i in range(0,n):
    	for j in range(0,n):
    		if (x[i]^y[j]) in z 
    			c = c + 1 
    if (c%2 == 0):
    	print ("Karen")
    else:
    	print ("Koyomi")
    	