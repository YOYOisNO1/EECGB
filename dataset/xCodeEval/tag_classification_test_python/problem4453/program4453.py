def program4453():
    import sys
    import math
    
    data = map(int, input().split())
    x = data[0]
    y = data[1]
    if x == y:
    	print("=")
    	sys.exit()
    if x == 1:
    	print("<")
    	sys.exit()
    if y == 1:
    	print(">")
    	sys.exit()
    
    if x < y:
    	t = x / math.log(x, y)
    	if t < y:
    		print(">")
    	elif t == y:
    		print("=")
    	else:
    		print("<")
    else:
    	t = y / math.log(y, x)
    	if t < x:
    		print("<")
    	elif t == x:
    		print("=")
    	else:
    		print(">")