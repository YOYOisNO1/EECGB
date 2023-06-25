def program3377():
    a,r,w=map(int,input().split())
    b=w%a
    if -a<r<a and w%a>0:
    	k=w/a
    	k=k+min(1,b)
    	if k==1:
    		if -a/2.0<r<a/2.0:
    			print 1
    		else:
    			print -1
    	else:
    		if (k%2==0):
                if (-a/2.0<r<a/2.0):
                    b=(k/2-1)*2+k/2+1
                    print b
                else:
                    print -1
    		elif k%2==1:
    			b=k/2
    			if -a<r<0:
    				print (b*2+(k-b)-1)
    			elif 0<r<a:
    				print (b*2+(k-b))
    			else: 
    				print -1
    		else:
    			print -1
    else:
    	print -1