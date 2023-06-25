def program3847():
    a = input()
    b = input()
    c = input()
    
    who = [
    	("paper", "rock"), # who win, who lose
    	("scissors", "paper"),
    	("rock", "scissors")
    ]
    
    if (a == b and a == c and b == c) or (a != b and a != c and b != c):
    	print("?")
    else:
    	if a == b:
    		if (a, c) in who:
    			print("?")
    		else:
    			print("S")
    	elif a == c:
    		if (a, b) in who:
    			print("?")
    		else:
    			print("M")
    	elif b == c:
    		if (b, a) in who:
    			print("?")
    		else:
    			print("F")