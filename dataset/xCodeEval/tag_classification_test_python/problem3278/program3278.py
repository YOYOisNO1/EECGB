def program3278():
    n = input()
    A = [input().split() for _ in range(n)]
    A = [ (int(x[0]),x[1]) for x in A]
    
    d = 0
    err = False
    for x in A:
    	# print(d,err)
    	if d==0 or d==20000:
    		if x[1]=='West' or x[1]=='East':
    			err = True
    	if x[1]=='South':
    		d+=x[0]
    	elif x[1]=='North':
    		d-=x[0]
    	if d<0 or d>20000:
    		err = True
    if d != 0:
    	err = True
    if err:
    	print('NO')
    else:
    	print("YES")