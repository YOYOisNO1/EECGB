    import math
    n = int(input())
    
def islucky(x):
    	a = map(int, list(str(x)))
    	b = [0, 1, 2, 3, 5, 6, 8, 9]
    	for i in b:
    		if a.count(i) != 0:
    			return False
    	return True
    
    for i in range(int(math.sqrt(n))+1):
    	if i != 0:
    		if (islucky(i) and (n%i == 0 or i%n == 0)) or islucky(n):
    			print 'YES'
    			exit(0)
    
    print 'NO'
    