    n=input()
def add(l, value):
    	for i in xrange(len(l)-1, value-1, -1):
    		l[i]=min(l[i], l[i-value]+1)
    if n>50:
    	result=49*n+1
    	l=[1000000000]*2000
    	l[0]=0
    	for i in xrange(20):
    		add(l, 4)
    		add(l, 9)
    	for i in xrange(40):
    		add(l, 49)
    	for i in xrange(30, 49*40):
    		if l[i]>40:
    			result-=1
    	for i in xrange(30):
    		if l[i]==1000000000:
    			result-=1
    else:
    	if n<0:
    		n=-n
    	result=49*n+1
    	l=[1000000000]*result
    	l[0]=0
    	for i in xrange(n):
    		add(l, 4)
    		add(l, 9)
    		add(l, 49)
    	for i in xrange(result):
    		if l[i]>n:
    			result-=1
    print(result)