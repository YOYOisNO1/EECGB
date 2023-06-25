def program2292():
    myString = input() ;stringLen = len(myString) ; decodedString = ""; item = 0
    while item < stringLen:
    	if myString[item] == ".":
    		decodedString += "0"; 
    		item += 1
    	elif myString[item] == "-":
    		if myString[item + 1] == ".":
    			decodedString += "1"
    		else:
    			decodedString += "2"
    		item += 2
    print(decodedString)