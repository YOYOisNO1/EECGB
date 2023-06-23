def program1981():
    letters = input()
    result = int(26)
    
    for i in range(len(letters - 1)):
    	result += 25;
    
    	if letters[i + 1] != letters[i]:
    		result++;
    
    print(result)