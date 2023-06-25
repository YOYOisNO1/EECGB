def program1782():
    n,m = map(int,input().split())
    while True:	
    	for i in range(1,n+1):
    		if m < i:
    			break
    		else:
    			m -= i
    print m