def program1973():
    n, k = map(long,input().split())
    l=[]
    k = min(k,100000)
    for x in range(1,k+1):
    	if (n%x) in l  :
    		print('No') 
    		exit(0)
    	l.append(n%x)
    print('Yes')