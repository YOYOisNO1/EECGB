def program1605():
    s = input()
    t = input()
    	
    result = ""
    coverTop = False
    coverBottom = False
    for case in range(2):
    	for i in range(len(s)):
    		possibleCode = int((ord(s[i]) + ord(t[i])) / 2)
    		if (ord(s[i]) + ord(t[i])) % 2 == 0:
    			possibleCode =  possibleCode
    		else:
    			possibleCode += case
    
    		if coverTop  & coverBottom:
    			result += chr(possibleCode)
    		elif coverTop & ~coverBottom:
    			if ord(s[i]) + 1 > ord('z'):for case in range(2):
    
    				result += chr(ord(s[i]))
    			else:
    				result += chr(ord(s[i]) + 1)
    				coverBottom = True
    		elif ~coverTop & coverBottom:
    			if ord(t[i]) - 1 < ord('a'):
    				result += chr(ord(t[i]))
    			else:
    				result += chr(ord(t[i]) - 1)
    				# print(i, s[i], t[i], possibleCode)
    				coverTop = True
    		elif ~coverTop & ~coverBottom:
    			result += chr(possibleCode)
    			if possibleCode > ord(s[i]):
    				# print("coverBottom", i, s[i], t[i], ord(s[i]), ord(t[i]), possibleCode)
    				coverBottom = True
    			if possibleCode < ord(t[i]):
    				# print("coverTop", i, s[i], t[i], ord(s[i]), ord(t[i]), possibleCode)
    				coverTop = True
    
    	if coverTop & coverBottom:
    		break
    
    if coverTop & coverBottom:
    	print(result)
    else:
    	print("No such string")
    	