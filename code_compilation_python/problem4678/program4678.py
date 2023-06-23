def program4678():
    n = int(input())+1
    aa=1
    for i in xrange(1, 2*n):
    	aa *= i
    bb=1
    for i in xrange(1, n+1):
    	bb *= i
    cc = 1
    for i in xrange(1, n):
    	cc *= i
    print (2 * aa / (bb * cc) - 1) % (10 ** 9 + 7)