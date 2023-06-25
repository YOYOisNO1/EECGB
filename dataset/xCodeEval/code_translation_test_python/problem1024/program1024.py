def program1024():
    import math
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])
    
    i = 1
    while a >= 0 and b >= 0:
    	if i % 2 == 0:
    		b -= i
    	else:
    		a -= i
    	i += 1
    
    if a < 0:
    	print('Vladik')
    else:
    	print('Valera')