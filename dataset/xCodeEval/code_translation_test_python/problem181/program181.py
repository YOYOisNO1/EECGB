def program181():
    n,k=map(int,input().split())
    
    l=0
    
    r=2*10**9
    
    while l<r:
    
    	m=(r+l)//2;s=0;t=1
    
    	while m//t:s+=m//t;t*=k
    
    	if s<n:l=m+1
    
    	else:r=m
    
    print(l)
    
    
    
    # Made By Mostafa_Khaled