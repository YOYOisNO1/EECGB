def program5509():
    a,x,y=map(int,input().split())
    r=y//a
    y=y%a
    if y == 0: print(-1)
    else:
    	if r == 0:
    		# one square on the vertical
    		if -a<x*2<a:print(1)
    		else:print(-1)
    	elif r % 2 == 1:
    		if -a<x*2<a:#cuz half
    			print(2+(r-1)//2*3)
    		else:
    			print(-1)
    	else:
    		if -a<x<0:print((r-2)//2*3+3)
    		elif 0<x<a:print((r-2)//2*3+4)
    		else:print(-1)
    		