    n = int(input())
def rad_n(n,x):
    	r =''
    	while x>n:
    		r=str(x%n)+r
    		x = x/n
    	r=str(x)+r
    	return r
    l = len(str(rad_n(n,(n-1)*(n-1))))
    #print l
    for i in xrange(1,n):
    	for j in xrange(1,n):
    		a = rad_n(n,i*j)
    		if j==1:
    			print a,
    		elif j<n-1:
    			print ' '*(l-len(a))+a,
    		else:
    			print ' '*(l-len(a))+a