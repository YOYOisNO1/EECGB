def program294():
    n = int(input())
    votes = list(map(int, input().split()))
    
    limak = votes[0]
    others = list(reversed(sorted(votes[1:])))
    bribes = 0
    
    while limak <= others[0]:
    	limak += 1
    	others[0] -= 1
    	bribes += 1
    	if others[0] < others[1]:
    		for i in range(2, len(others)):
    			if others[i] <= others[0]:
    				others[i-1], others[0] = others[0], others[i-1]
    				break
    		else:
    			others[0], others[-1] = others[-1], others[0]
    print(bribes)