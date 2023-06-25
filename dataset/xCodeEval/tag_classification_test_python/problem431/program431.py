def program431():
    h, N = tuple(int(i) for i in input().split())
    L = 1
    R = pow(2,h)
    mode = 0
    level = 0
    ans = 0
    while(L!=R):
    	M = (L+R)//2
    	if(N<=M):
    		if(mode==0):
    			mode = 1
    			ans+=1
    		else:
    			ans+=pow(2,h-level)
    		R = M
    	else:
    		if(mode==0):
    			ans+=pow(2,h-level)
    		else:
    			mode = 0
    			ans+=1
    		L = M+1
    	level+=1
    print(ans)