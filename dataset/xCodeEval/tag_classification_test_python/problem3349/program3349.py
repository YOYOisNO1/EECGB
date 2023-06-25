def program3349():
    n = int(input())
    R_to_O = int(input())
    R_to_E = int(input())
    O_to_E = int(input())
    position = "R"
    distance = 0
    while n>1:
    	if position == "R":
    		if R_to_O > R_to_E:
    			distance += R_to_E
    			position = "E"
    		else:
    			distance += R_to_O
    			position = "O"
    	elif position == "O":
    		if O_to_E > R_to_O:
    			distance += R_to_O
    			position = "R"
    		else:
    			distance += O_to_E
    			position = "E"
    	elif position == "E":
    		if O_to_E > R_to_E:
    			distance += R_to_E
    			position = "R"
    		else:
    			distance += O_to_E
    			position = "O"
    	n -= 1
    print(distance)
    
    	