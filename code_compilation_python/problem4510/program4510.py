def program4510():
    s = input()
    sm = sum([int(x) for x in s])
    
    fib = [0] * 20
    fib[0] = 0
    fib[1] = 1
    fib[2] = 1
    
    for i in range(3, 20):
    	fib[i] = fib[i-1] + fib[i-2]
    
    sf = set(fib)
    	
    if sm in sf:
    	print "Yes"
    else:
    	print "No"