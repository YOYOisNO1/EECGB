def fat(x):
    	if x == 1:
    		return 1
    	else:
    		return x * fat(x - 1)
    
    a, b = map(int,input().split())
    if a > b:
    	print(fat(b))
    else:
    	print(fat(a))