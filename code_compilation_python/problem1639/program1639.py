def program1639():
    import sys
    #sys.stdin = open("in.txt", "r")
    
    n = input()
    a = map(int, input().split())
    if n < 3:
    	print "no"
    else:
    	b = []
    	for i in xrange(n-1):
    		b.append([a[i], a[i+1])
    	good = False
    	for i in xrange(n-1):
    		for j in xrange(i+1, n-1):
    			t1 = b[i][0] > b[j][0] and b[i][0] < b[j][1] and b[i][1] > b[j][1]
    			t2 = b[i][1] > b[j][0] and b[i][1] < b[j][1] and b[i][0] < b[j][0]
    			if t1 or t2
    				good = True
    				break
    	if good:
    		print "yes"
    	else:
    		print "no"