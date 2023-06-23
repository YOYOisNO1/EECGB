def program829():
    b = input()
    	a = input()
    	i = int(b)
    	if 'ogo' not in a:
    		print(a)
    		exit()
    	x = ''
    	while i != 0:
    		if 'o'+('go' * i) in a:
    			x = a.replace('o' + ('go' * i), '***')
    			a = x
    		i -= 1
    	print(x)