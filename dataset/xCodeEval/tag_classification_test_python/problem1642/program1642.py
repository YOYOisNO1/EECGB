def program1642():
    a1=int(input())
    a2=int(input())
    k1=int(input())
    k2=int(input())
    n=int(input())
    
    x=a1*(k1-1)+a2*(k2-1)
    if(x>=n):
    	min1=0
    else:
    	min1=n-x
    	
    if(k1<k2):
    	d1=n//k1
    	if(d1>=a1):
    		d1=a1
    	d2=(n-(d1*k1))//k2
    else:
    	d2=n//k2
    	if(d2>=a2):
    		d2=a2
    	d1=(n-(d2*k2))//k1
    if(d1>=a1):
    	d1=a1
    if(d2>=a2):
    	d2=a2
    print(min1,d1+d2)