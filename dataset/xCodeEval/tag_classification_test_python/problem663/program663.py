def program663():
    s = input().strip()
    ans = -1
    val = 1
    for i in xrange(len(s)):
    	if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' or s[i] == 'Y':
    		val = 1
    	else:
    		val+=1
    	ans = max(ans, val)
    	#print(i,) ans
    print(ans)