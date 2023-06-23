def f(n):
    	n = n + 1
    	while n%10 == 0:
    		n = n // 10	
    	return n
    
    num = int(input())
    if num < 10:
    	print(9)
    	exit(0)
    
    a = set()
    result = 0
    while(! num in a):
        a.add(num)
    	num = f(num) 
    	
    
    print(len(a))