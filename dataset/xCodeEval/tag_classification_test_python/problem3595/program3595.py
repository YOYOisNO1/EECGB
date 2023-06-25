def program3595():
    # coding: utf-8
    
    tam, time = map(int, input().split())
    
    ans = input()
    string = []
    
    for k in xrange(tam):
    	string.append(ans[k])
    
    for i in xrange(time):
    	j = 0
    	while True:
    		if j == tam:	break
    
    		if string[j] == 'B':
    			if j + 1 < tam and string[j + 1] == 'G':
    				string[j], string[j + 1] = string[j + 1], string[j]
    				j += 1
    
    		j += 1
    
    ans = ""
    for k in xrange(tam):
    	ans += string[k]
    
    print(ans)