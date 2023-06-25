def program230():
    s = input()
    
    
    j = 0
    
    for i in range(len(s)):
    	if j == 0 and s[i] == 'h':
    		j += 1
    	elif j == 1 and s[i] == 'e':
    		j += 1
    	elif (j == 2 or j == 3 )and s[i] == 'l':
    		j += 1
    	elif j == 4 and s[i] == 'o':
    		j += 1
    print("YES" if j== 5 else "NO" )