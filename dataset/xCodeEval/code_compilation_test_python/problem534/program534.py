def program534():
    l = list(map(int, input().split()))
    s = set(l)
    if len(s) == 1:
    	print('Elephant')
    elif len(s) == 2:
    	if l.count(l[0]) == 5 || l.count(l[0]) == 1:
    		print('Bear')
    	else:
    		print('Elephant')
    elif len(s) == 3:
    	print('Bear')
    else:
    	print('Alien')