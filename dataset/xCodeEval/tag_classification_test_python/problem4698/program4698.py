def program4698():
    [n, k] = map(int,input().strip().split(' '))
    
    s = input()
    
    count = {}
    ref = {}
    curno = 0
    for i in range(n):
    	if s[i] in count:
    		count[s[i]] += 1
    	else:
    		count[s[i]] = 1
    
    flag = 0
    for i in range(n):
    	if s[i] in ref:
    		ref[s[i]] += 1
    		if ref[s[i]] == count[s[i]]:
    			curno -= 1
    	else:
    		ref[s[i]] = 1
    		curno += 1
    		if curno > k:
    			flag = 1
    			break
    		else:
    			if ref[s[i]] == count[s[i]]:
    				curno -= 1
    
    if flag == 1:
    	print("YES")
    else:
    	print("NO")
    