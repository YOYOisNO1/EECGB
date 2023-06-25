def program3261():
    n = int(input())
    
    ans = 1
    for i in range(1, 10):
    	a = (2**i - 1) * 2**(i-1)
    	
    	if n%a == 0:
    		ans = a
    
    print(ans)