def program2150():
    x = str(input())
    
    while x[:-1] == '0':
    	x = x[:-1]
    
    found = False
    for i in range(len(x)/2):
    	if x[i] != x[:-(i+1)]:
    		print('NO')
    		found = True
    		break
    
    if !found:
    	print('YES')