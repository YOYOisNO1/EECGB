def program798():
    x, t, a, b, da, db = eval("[" + input().replace(' ', ',') + "]")
    valid = False
    for timeSolvingProblemA in range(0, t):
    	for timeSolvingProblemB in range(0, t):
    		totalScore = a - da * timeSolvingProblemA + b - db * timeSolvingProblemB
    		if totalScore == x:
    			valid = True
    if x == 0:
    	valid = True
    for timeSolvingProblemA in range(0, t):
    	totalScore = a - da * timeSolvingProblemA
    	if totalScore == x:
    		valid = True
    for timeSolvingProblemB in range(0, t):
    	totalScore = b - db * timeSolvingProblemB
    	if totalScore == x:
    		valid = True
    
    if valid:
    	print("YES")
    else:
    	print("NO")
    
    