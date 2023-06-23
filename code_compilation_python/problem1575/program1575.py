def program1575():
    n = int(input())
    m = [int(x) for x in input().split()]
    a = m[0]
    s = 0
    br = 0
    for i in range(n-1):
        b = m[i+1]
    	if a==1:
    	    if b==2:
    		    s+=3
    		else:
    			s+=4
    	elif a==2:
    		if b==1:
    			s+=3
    		else:
    			br = 1
    			break
    	else:
    		if b==1:
    			s+=4
    		else:
    			br = 1
    			break
    if br==1:
    	print('Infinite')
    else:
    	print('Finite')
    	print(s)