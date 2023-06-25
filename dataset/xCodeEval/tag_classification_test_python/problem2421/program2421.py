def program2421():
    
    if __name__=='__main__':
    	n = int(input())
    	s = input().replace('(', "_(_").replace(')', "_)_")
    	l = 0
    	in_bracket = False
    	count = 0
    	for w in s.split('_'):
    		if w == "":
    			continue
    		if w == "(":
    			in_bracket = True
    			continue
    		if w == ")":
    			in_bracket = False
    			continue
    		if in_bracket:
    			count += 1
    		else:
    			l = max(l, len(w))
    	print(l, count)