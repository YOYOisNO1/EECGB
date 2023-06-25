def program2257():
    #intnog
    
    h1,h2 = map(int, input().split())
    a,b = map(int, input().split())
    
    speed = a-b
    h = h2-h1
    if 8 * a >= h:
    	print(0)
    	exit()
    if speed <= 0:
    	print(-1)
    	exit()
    h -= 12*speed
    i = 1
    while True:
    	if 8*a >= h:
    		print(i)
    		exit()
    	h = h - 12*speed
    	i += 1