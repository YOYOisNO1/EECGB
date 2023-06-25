def program4793():
    n = int(input())
    home = input()
    
    ida = volta = 0
    
    while True:
    	try:
    		voo = input()
    	except Exception:
    		break
    
    	if voo[:3] == home:
    		ida += 1
    	elif voo[5:] == home:
    		volta += 1
    
    if ida == volta:
    	print("home")
    else:
    	print("contest")