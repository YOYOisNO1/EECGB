def program2682():
    # your code goes here
    l=[]
    for i in xrange(3):
    	l+=[map(float, input().split())]
    if (l[0][0]==l[1][0] and l[1][0]==l[2][0]) or (l[0][1]==l[1][1] and l[1][1]==l[2][1]): print(1)
    else:
    	l.sort()
    	if l[0][1]==l[1][1] or l[1][1]==l[2][1] or (l[2][1]==l[0][1] and (l[0][0]==l[1][0] or l[1][0]==l[2][0])): print(2)
    	else:
    		l.sort(key = lambda x: x[1])
    		if l[0][0]==l[1][0] or l[1][0]==l[2][0]: print(2)
    		else: print(3)