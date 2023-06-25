def program4800():
    s=input().split()
    a,h,w=int(s[0]),int(s[1]),int(s[2])
    if(a>h)|(a>w):
    	print-1
    else:
    	k=abs(h-w)
    	if k==0:
    		k=h
    	if k<a:
    		print-1
    	else:
    		c=k//a
    		print float(k)/c-a