def program3828():
    import itertools
    import sys
    
    [n] = [int(x) for x in sys.stdin.readline().split()]
    dice = []
    
    for i in range(n):
    	dice.append([int(x) for x in sys.stdin.readline().split()])
    
    i = 1
    
    while i < 10 ** n:
    	x = i
    	dig = []
    
    	while x != 0:
    		dig.append(x % 10)
    		x /= 10
    
    	if not any(all(dig[i] in permdice[i] for i in range(len(dig))) for permdice in itertools.permutations(dice)):
    		break
    
    	i += 1
    
    print(i) - 1
    
    '''
    ===
    3
    0 1 2 3 4 5
    6 7 8 9 0 1
    2 3 4 5 6 7
    ---
    87
    ===
    3
    0 1 3 5 6 8
    1 2 4 5 7 8
    2 3 4 6 7 9
    ---
    98
    ===
    '''