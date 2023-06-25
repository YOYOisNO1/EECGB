def program2955():
    #!/usr/bin/env python
    from string import split
    from math import sqrt
    
    x, y = map(int, split(input()))
    
    dist = sqrt(x ** 2 + y ** 2)
    if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
    	if 0 <= dist % 2 <= 1:
    		print('black')
    	else:
    		print('white')
    else:
    	if 1 <= dist % 2 or dist % 2 == 0:
    		print('black')
    	else:
    		print('white')