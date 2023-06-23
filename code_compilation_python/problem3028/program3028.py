    
    
def ncr(n,r):
    	return(fact(n)/(fact(r)*fact(n-r)))
def fact(n):
    	res=1
    	for i in range(2,n+1):
    		res=res*i
    	return res
    
    l1=list(input())
    l2=list(input())
    c1=0
    c2=0
    c3=0
    for k in range(len(l1)):
    	if(l1[k]=='+'):
    		c1+=1
    	if(l2[k]=='+'):
    		c2+=1
    	if(l2[k]=='?'):
    		c3+=1
    a=c1-c2
    
    if(c3>=a):
    	a1=ncr(c3,a)
    	print(a1/(2**c3)
    else:
    	print(0/(2**c3))
    
    
    
    
    
    
    
    
    
    
    
    