def program2260():
    h1 ,h2 = map(int,input().split())
    a, b = map(int,input().split())
    
    if a <= b:
    	if h1 + (8*a) >= h2:
    		print(0)
    	else:
    		print(-1)
    else:
    	cnt = 0
    	h = h1
    	h = h1 + 8*a
    	while(h < h2):
    		h = h - 12*b
    		h = h + 12*a
    		cnt += 1
    	print(cnt)