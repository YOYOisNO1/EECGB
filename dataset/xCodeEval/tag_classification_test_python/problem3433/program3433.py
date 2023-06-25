def solve():
    	string = input().strip()
    	number = int(string, 2)
    	current = 0
    	normal = 4
    	missed = 1
    	while True:
    		normal = (4 ** current)
    		if normal >= number:
    			break
    		missed += 1
    		current += 1
    
    	return missed - 1
    
    
    
    print(solve())