def program386():
    s=input().split()
    n=int(s[0])
    a=int(s[1])
    b=int(s[2])
    c=int(s[3])
    
    nn=0
    k=0
    while nn==0:
    
    	if n%4==0:
    		break
    	n+=1
    	k+=1
    if k==0:
    	print(0)
    else:
    	if k==1:
    		res=[a,b+c,3*c]
    		print(min(res))
    	elif k==2:
    		res=[2*a,b,c*2]
    		print(min(res))
    	else:
    		res=[3*a,c,b+a,3*b+a]
    		print(min(res))