def program1927():
    #!/usr/bin/env python
    
    n,m = map(lambda x: int(x)+1,input().split())
    twos = range(2,n*2,2)
    threes = range(3,m*3,3)
    overlap = len(list(set(twos)&set(threes)))
    
    if overlap:
    	maxtwos = twos[-1]
    	maxthrees = threes[-1]
    	while overlap>0:
    		if maxtwos <= maxthrees:
    			maxtwos += 2
    		else:
    			maxthrees += 3
    		overlap -= 1
    
    	print max(maxthrees, maxtwos)
    else:
    	print max(twos + threes)