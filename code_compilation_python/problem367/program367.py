     from collections import Counter
    
def boy_Or_Girl():
    	s = input()
    	c = Counter(s)
    	l = len(c.keys())
    	if l % 2 == 0:
    		return "CHAT WITH HER!"
    	else:
    		return "IGNORE HIM!"
    
def main():
    	print boy_Or_Girl()
    main()