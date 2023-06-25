def gcd(a,b):
    	if a%b == 0:
    		return b
    	else:
    		return gcd(b,a%b)
    s=input().split()
    a,h,w=int(s[0]),int(s[1]),int(s[2])
    if(a>h)|(a>w):
    	print-1
    else:
    	k=gcd(h+a,w+a)
    	c=k//a
    	if c==0:
    		print-1
    	else:
    		print float(k)/c-a