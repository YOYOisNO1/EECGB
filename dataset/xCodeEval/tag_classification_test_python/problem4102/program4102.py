def from_same_letters(word):
    	if len(word) == 0:
    		return True
    
    	char = word[0]
    
    	for letter in word:
    		if letter != char:
    			return False
    
    	return True
    
    letters = input()
    result = int(51)
    
    for i in range(len(letters) - 1):
    	result += 25;
    
    	if letters[i + 1] != letters[i]:
    		++result;
    
    print(result)