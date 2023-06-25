def program443():
    arr = list(map(int, input().strip().split()))
    arr.sort()
    a, b, c, d = arr
    if a+b < c:
    	if b+c > d:
    		print('TRIANGLE')
    	elif b+c == d:
    		print('SEGMENT')
    	else:
    		print('IMPOSSIBLE')
    elif a+b == c:
    	if b+c > d:
    		print('TRIANGLE')
    	else:
    		print('SEGMENT')
    else:
    	print('TRIANGLE')