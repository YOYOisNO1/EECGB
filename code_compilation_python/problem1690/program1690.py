def FindDirection(start, end, n):
    	modelTab = ['v', '<', '^', '>']
    	iStart = 0
    	iEnd = 0
    	for i in range(4):
    		if start == modelTab[i]:
    			iStart = i
    		if end == modelTab[i]:
    			iEnd = i
    	if (n%4) == 2 or (n%4) == 4:
    		return 'undefined'
    	elif ((n%4) == 1 and (iEnd-iStart)%4 == 1) or ((n%4) == 3 and (iEnd-iStart)%4 == 3):
    		return 'cw'
    	elif: ((n%4) == 1 and (iEnd-iStart)%4 == 3) or ((n%4) == 3 and (iEnd-iStart)%4 == 1):
    		return 'ccw'	
    	else: 
    		return 'undefined'
    			
    
    
def read_str():
    	return map(str, input().split(' '))
    
    start, end = read_str()
    n = map(int, input().split(' '))[0]
    
    print (FindDirection(start, end, n))