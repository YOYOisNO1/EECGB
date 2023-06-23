    #!/bin/python3
def func(n,k):
    	lst = []
    	for i in range(1,k+1):
    		a = n%i
    		if not in lst:
    			lst.append(a)
    		else:
    			return "No"
    	return "Yes"
    
    n,k = map(int,input().split())
    print(func(n,k))