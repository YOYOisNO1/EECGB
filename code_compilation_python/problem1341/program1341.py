def program1341():
    a, b, x = map(int, input().split())
    
    string = ""
    curr = 0 if a > b else 1
    while x > 0:
    	
        string += str(curr)
    	x -= 1
    	
        if curr == 0:
            a -= 1
    	else:
            b -= 1
    	
        if x > 0:
            curr = 1 - curr
    
    if curr == 0:
    	string += str(curr) * a + str(1 - curr) * b
    else:
    	string += str(curr) * b + str(1 - curr) * a
    
    print(string)