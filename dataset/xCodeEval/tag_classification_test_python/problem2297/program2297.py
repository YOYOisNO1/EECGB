def program2297():
    s = list(input())
    i = 0
    while i < len(s)-1:
    	if s[i] == '.':
    		print(0,end="")
    	else:
    		if s[i] == '-' and s[i+1] == '-':
    			print(2,end="")
    		else:
    			print(1,end="")
    		i += 1
    	i += 1
    if i == len(s) - 1:
    	print(0,end="")