def program6514():
    a,b,pos=map(int,input().split())
    
    for i in range(b):
    	a*=10
    	c=a//b
    	a=a%b
    	if c==pos:
    		print(i+1)
    		exit()
    print("-1")