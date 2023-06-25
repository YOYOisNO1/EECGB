    import math
def primenum(x):
    	count=0
    	for i in range(2,int(math.floor(math.sqrt(x)))+1):
    		if(x%i==0):
    			count=count+1
    	if(count==0):
    		return True
    	else:
    		return False
    
    n=int(input())
    if(n==1):
    	print(1,1)
    elif(primenum(n)==True):
    	print(1,n)	
    else:
    	a=[]
    	for i in range(2,int(math.ceil(math.sqrt(n))+1)):
    		if(n%i==0):
    			a.append(i)
    	x=a[len(a)-1]
    	print(min(x,n//x),max(x,n//x))