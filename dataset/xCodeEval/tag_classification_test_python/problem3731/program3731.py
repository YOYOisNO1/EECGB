def program3731():
    import math
    n,t,k,d=map(int,input().split())
    MT=math.ceil(n/k)
    M=0;R=0;i=0
    while i<n:
    	M+=1
    	R+=t
    	if R>d or t>d:
    		R+=t
    		i+=k
    	i+=k
    
    
    if M<MT:
    	print("YES")
    else:
    	print("NO")