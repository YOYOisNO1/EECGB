def program683():
    n,m=map(int,input().split())
    s=0
    t=0
    if n==0 and m!=0:
    	print("Impossible")
    elif m==0:
    	print(n,end=" ")
    	print(n)
    elif n>=m:
    	s=n
    	t=n+m-1
    	print(s,end=" ")
    	print(t)
    else:
    	if m//n==1:
    		
    		print(n+m%n,end=" ")
    		print(n+m-1)
    	else:
    		print(n*(m//n)+m%n,end=" ")
    		print(n+m-1)
    	