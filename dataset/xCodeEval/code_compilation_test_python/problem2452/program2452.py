def program2452():
    n = input ()
    sum = 0
    i = 1
    while True :
    	sum = sum + 5 * i
    	if sum > n :
    		m = ( sum - n ) / i
    		if  m == 0 :
    			print "Howard"
    		elif m == 1 :
    			print "Rajesh"
    		elif m == 2 :
    			print "Penny"
    		elif m == 3 :
    			print "Leonard"
    		else :
    			print "Sheldon"
    	else
    		i += 1