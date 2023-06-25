def program1039():
    l,r = map(int,input().split())
    if l -r == 0:
    	print l
    else if l - r > 1:
    	if (l-r)%2 == 0:
    		print 2
    	else:
    		print 3
    else:
    	print 2 