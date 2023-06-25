def program3118():
    a = int(input())
    s = input()
    b = s.split()
    i = 0
    s = b[0]
    if s[0] == '1':
    	while i < a:
    		if s[i] == '0':
    			i += 1
    			break 
    		i += 1		
    	print(i)
    else:
    	print(1)