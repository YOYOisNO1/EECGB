def program106():
    d = {'q': 9, 'r': 5, 'b': 3, 'n': 3, 'p': 1, 'k': 0}
    
    b = 0
    w = 0
    
    for _ in range(8):
    	temp = input()
    	for i in temp:
    		if i != '.':
    			if i.islower():
    				b += d[i.lower()]
    			else:
    				w += d[i.lower()]
    if b == w:
    	print("Draw")
    elif b > w:
    	print("Black")
    else:
    	print("White")