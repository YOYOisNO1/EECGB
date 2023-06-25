def program2939():
    import sys
    
    s = sys.stdin.readline().rstrip()
    
    bool haslower = False
    bool hasupper = False
    bool hasdigit = False
    for c in s:
    	if c.isdigit():
    		hasdigit = True
    	elif c.isupper():
    		hasupper = True
    	elif c.islower():
    		haslower = True
    if hasupper and haslower and hasdigit and len(s) >= 5:
    	print("Correct")
    else:
    	print("Too weak")