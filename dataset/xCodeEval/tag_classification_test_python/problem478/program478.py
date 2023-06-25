def program478():
    string = input()
    new_string = []
    
    for i in range(10):
    	new_string.append(string[i * 10: i * 10 + 10])
    
    y = []
    
    for i in range(10):
    	y.append(input())
    
    for i in range(len(new_string)):
    	for e in range(len(new_string)):
    		if y[e] in new_string[i]:
    			print(e, end = "")