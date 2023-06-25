def program4074():
    import sys,os
    n=int(sys.stdin.readline())
    p=sys.stdin.readline().split()
    for i in range(n):
    	p[i]=int(p[i])
    c=sys.stdin.readline().split()
    a=[]
    for i in range(len(c)):
    	c[i]=(int(c[i]), i)
    	a.append(0)
    c.sort()
    r=0
    for i in range(n):
    	r+=p[i]
    	k=len(c)-1
    	while k>=0:
    		if r>=c[k][0]:
    			a[c[k][1]]+=(r/c[k][0])
    			r-=(r/c[k][0])*c[k][0]
    		k-=1
    for i in range(len(a)):
    	sys.stdout.write(str(a[i])+' ')
    sys.stdout.write('\n')
    print(r)