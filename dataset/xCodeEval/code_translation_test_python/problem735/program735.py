def program735():
    s = input()
    score = 0
    moves = 0
    c = s[0]
    r = s[1]
    
    if c == "a" or c == "h":
    	score += 1
    if r == "1" or r == "8":
    	score += 1
    	
    if score == 2:
    	moves = 3
    elif score == 1:
    	moves = 5
    else:
    	moves = 8
    
    print(moves)