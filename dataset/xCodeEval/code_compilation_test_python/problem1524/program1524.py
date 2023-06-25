    Read = lambda:map(int,input().split())
    a,b,n = Read()
    cur=0
def gcd(a,b):
    	if b==0 : return a
    	else : return gcd(b,a%b)
    while 1:
    	t = gcd((cur*b+(1-cur)*a),n)
    //	print "cur=%d a=%d b=%d t=%d n=%d" %(cur,a,b,t,n)
    	if t>n :
    		print 1-cur
    		break
    	else: n-=t
    	cur = 1-cur