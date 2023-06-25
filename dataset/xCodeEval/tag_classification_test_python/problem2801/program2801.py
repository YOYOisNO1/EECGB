def comb(n):
    	if n == 1:
    		return [0, 1, 2]
    	elif n == 2:
    		return [1, 0, 2]
    	elif n == 3:
    		return [1, 2, 0]
    	elif n == 4:
    		return [2, 1, 0]
    	elif n == 5:
    		return [2, 0, 1]
    	else:
    		return [0, 2, 1]
    
    
    n = int(input())
    x = int(input())
    
    n = n % 6 + 1
    c = comb(n)
    print(c[x])
    
    