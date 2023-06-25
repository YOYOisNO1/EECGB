def get_int(string, n):
    	i = j = k = 0
    	for s in string:
    		k += 1
    	for s in string:
    		if i == n - 1:
    			break
    		if s == ' ':
    			i += 1
    		j += 1
    	i = 0
    	while j < k:
    		if string[j] == ' ':
    			break
    		i = 10 * i + int(string[j])
    		j += 1
    	return i
    
def get_zcy(string):
    	strin = ''
    	for i in string:
    		strin = i + strin
    	return string + strin
    	
    x = input()
    k = get_int(x, 1)
    p = get_int(x, 2)
    sum = 0
    
    for i in range(1, k + 1):
    	y = f"{i}"
    	y = get_zcy(y)
    	sum += int(y)
    	
    print(sum % p)