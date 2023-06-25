def program65():
    n,a,b,c = map(int,input().split())
    if n%4==0:
    	print(0)
    else:
    	s=4-n%4
    	if s==1:
    		print(min(a,b+c,c*3))
    	elif s==2:
    		print(min(a*2,b,c*2))
    	else:
    		print(min(a*3,a+b,c))