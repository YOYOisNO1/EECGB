def program461():
    a, b = map(int, input().split())
    
    while True: 
    	if a == 0 or b == 0:
    		break 
    	elif a >= 2*b:
    		qtd = a//(2*b)
    		a -= qtd*2*b
    	elif b >= 2*a:
    		qtd = b//(2*a)
    		b -= qtd*2*a
    	else:
    		break
    print(a, b)
    