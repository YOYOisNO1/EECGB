def program3276():
    import sys
    n = input()
    
    x, y = 0, 0
    
    for i in xrange(n):
    	inp = input().split()
    	distance = int(inp[0])
    	direction = inp[1]
    
    	if direction == "South":
    		y += distance
    	elif direction == "North":
    		y -= distance
    	elif direction == "East":
    		if y == 0 or y == 20000:
    			print("NO")
    			sys.exit()
    		x += (distance % 40000)
    		
    	elif direction == "West":
    
    		if y == 0 or y == 20000:
    			print("NO")
    			sys.exit()
    
    		x -= (distance % 40000)
    
    	if y < 0 or y > 20000:
    		print("NO")
    		sys.exit()
    
    print("YES") if y == 0 else "NO"