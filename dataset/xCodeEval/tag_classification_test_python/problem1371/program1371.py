def program1371():
    first = input().strip()
    second = input().strip()
    first = [first[i] for i in range(len(first))]
    second = [second[i] for i in range(len(second))]
    p = []
    c = 0
    for i in range(len(first)):
    	if first[i] == '0' and second[i] == '0' and i > 0:
    		if first[i-1] == '0':
    			c+=1
    			first[i] = second[i] = first[i-1] = 'X'
    		elif second[i-1] == '0':
    			c+=1
    			first[i] = second[i] = second[i-1] = 'X'
    	if first[i] == '0' and second[i] == '0' and i < len(first)-1:
    		if first[i+1] == '0':
    			c+=1
    			first[i] = second[i] = first[i+1] = 'X'
    		elif second[i+1] == '0':
    			c+=1
    			first[i] = second[i] = second[i+1] = 'X'
    print(c)