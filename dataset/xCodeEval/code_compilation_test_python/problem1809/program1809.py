def program1809():
    str1 = input()
    str2 = input()
    
    l = len(str1)
    num = []
    
    for i in range(0, l) : 
    	num.append(0)
    	if str1[i] == '0' : num[i] = num[i] + 1
    	if str2[i] == '0' : num[i] = num[i] + 1
    
    now = 0
    res = 0
    for i in num : 
    	now = now + i
    	if now >= 3 : 
    		res = res + 1
    		now = now - 3
    	elif now <= 2 && i != 2 :
    		now = i
    
    print(res)