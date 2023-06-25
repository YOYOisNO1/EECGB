    
    
    
def main():
    	n = int(input())
    	s = input()
    	two_pos = False
    	if s[0] == '?' or s[-1] == '?':
    		two_pos = True
    
    	for i in range(len(s)-1):
    		if s[i] != '?' and s[i] == s[i+1]:
    			return False
    		if s[i] == '?' and s[i+1] == '?':
    			two_pos = True
    		if i > 0 and s[i] == '?' and s[i-1] == s[i+1]:
    			two_pos = True
    	
    	return two_pos
    
    if main():
    	print("Yes")
    else:
    	print("No")
    
    
    
    
    
    
    
    
    
    
    