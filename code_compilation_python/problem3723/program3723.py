def program3723():
    n=input()
    b=30
    while b >= 0:
        if 1<<b & n:
    		print b+1
    	print 1<<b
        b -= 1