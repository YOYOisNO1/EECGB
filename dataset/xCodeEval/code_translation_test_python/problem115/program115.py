def program115():
    t, s, x = map(int, input().split())
    
    if t == x:
    	print('YES')
    else:
    	if x==t:
    		print('YES')
    	elif (x-t)%s in [0,1] and (x-t)>=0 and x!=t+1 :
    		print('YES')
    	else:
    		print('NO')	