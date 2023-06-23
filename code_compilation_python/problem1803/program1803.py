def program1803():
    
     n = int(input())
    a = [int(x) for x in input().split()]
    kn = 0
    for i in a:
    	if i == 0:
    		kn += 1
    if kn > n // 2:
    	print(0)
    else:
    	ko = 0
    	kp = 0
    	for i in a:
    		if i < 0:
    			ko +=1
    		else:
    			if i != 0:
    				kp += 1
    	if ko =< n // 2 and kp =< n // 2:
    	    print(0)
    	    exit()
    	if ko == kp:
    		print(1)
    		exit()
    	if ko > kp:
    		print(-1)
    	else:
    		print(1)