    from sys import stdin, stdout  
    
    n=input()
    
    x0,y0=0,0
    sx,sy,s2=0,0,0
    
    x=[0]*n
    y=[0]*n
    
    for i in xrange(n):
    	px,py=map(int,input().split())
    	x[i],y[i]=px,py
    	sx+=px
    	sy+=py
    	s2+=x[i]*x[i]+y[i]*y[i]
    
    
    for i in xrange(n):
    	if (n*x[i],n*y[i])!=(sx,sy):
    		p,q=x[i],y[i]
    		break
    
    m=input()
    a=2*p*n-2*sx
    b=2*q*n-2*sy
    pc=n*(p*p+q*q)-s2
    pdt=-(a*a*p*p+2*a*b*p*q+b*b*q*q)
    sr=a*a+b*b
    
def isqrt(x):
        nn = int(x)
        if nn == 0:
            return 0
        fa, fb = divmod(nn.bit_length(), 2)
        x = 2**(fa+fb)
        while True:
            y = (x + nn/x)/2
            if y >= x:
                return x
            x = y
    pans=[]
    
    for i in xrange(m):
    	d=map(int,input().split())
    	sd=sum(d)
    	ans=[]
    	for j in xrange(n):
    		if j>=1 and d[j]==d[j-1]: continue
    		c=pc+sd-n*d[j]
    		dt=pdt+a*a*d[j]+2*a*c*p+b*b*d[j]+2*b*c*q-c*c
    		if dt<0: continue
    		idt=isqrt(dt)
    		if idt*idt!=dt:
    			continue
		def check(idt):
    			x=(b*idt-a*b*q+a*c+b*b*p)
    			y=(-a*idt+a*a*q+b*c-a*b*p)
    			if x%sr!=0:
    				return
    			ans.append([x/sr,y/sr])
    		check(idt)
    		if idt!=0: check(-idt)
    	ans.sort()
    	pans.append(len(ans))
    	for x in ans:
    		pans.append(x[0])
    		pans.append(x[1])
    
    stdout.write(" ".join(map(str,pans)))