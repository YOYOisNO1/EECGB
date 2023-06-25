    import math
    
def ii():
    	return map(int,input().split())
    
    n = input()
    count = 0
    count += int(math.log(n,2))
    n -= 2**count
    if n == 1:
    	count += 1
    else:
    	count += int(math.log(n,2))
    
    print count