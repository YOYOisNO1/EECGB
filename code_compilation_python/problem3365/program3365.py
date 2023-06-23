def program3365():
    n, m = map(int,input().split())
    if n >= 1 and m <= 100:
    	if n == m and n%2 == 0:
    		print "Malvika"
    	elif n == m and n%2 != 0:
    		print "Akshat"
    	elif n != m and n%2 != 0 and m%2 != 0 :
    		print "Akshat"
    	elif n!= m and n%2 == 0 and m%2 == 0:
    		print "Malvika"
    	elif n == 1 or m == 1
    		print "Akshat"
    	else: 
    		print "Malvika"