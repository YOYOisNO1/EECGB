def docfile():
    
    	f = open('', 'r')
    	line = f.readline()
    
    	return line
    
    if __name__ == "__main__":
    
    	word = input()
    
    	while word == word[::-1]:
    		word == word[0:-1]
    	return len(word)