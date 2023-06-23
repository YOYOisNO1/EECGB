def program1233():
    
    n = int(input())
    l = list(input())
    while True:
    
    	for i in range(len(l)-1):
    		if l[i] == 'U' and l[i + 1] == 'R' or l[i] == 'R' and l[i + 1] == 'U':
    			l[i] = 'D'
    			l.pop(i+1)
    			break
    
    		if i == len(l) - 2:
    			print(len(l))
    			exit()
    