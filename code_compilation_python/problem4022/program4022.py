def program4022():
    p1,p2,p3,p4,a,b=map(int,input().split())
    ans=0
    for no in xrange(a,b+1):
    	if no<p1 && no<p2 && no<p3 && no<p4:
    		ans+=1
    print ans