def program1106():
    
    n,a,b = map(int,input().split())
    count=1
    a=a+a%2
    b=b+b%2
    
    #1.2 34 56 78 
    #2 4 6 8 
    #2 8
    
    while a!=b:
    	#until two remains 1 2
    	a/=2
    	b/=2
    	a+=a%2
    	b+=b%2
    	count+=1
    
    
    if count**2=n:
    	
    
    	print("Final!")
    else:
    	print(count)