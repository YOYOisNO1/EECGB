def program602():
    n,m=map(int,input().split())
    if n==0 and m!=0:
    	print('Impossible')
    elif m<=n:
    	print(n,end=' ')
    	# print(m+n-1)
    
    elif m>n:
    	print(m,end=' ')
    	# print(m+n-1)
    if m!=0 and n!=0:
    	print(m+n-1)
    elif m==0 :
    	print(n)