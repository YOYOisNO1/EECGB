    #!/usr/bin/env python2
    
    from itertools import permutations
    
def read_ints():
    	return map(int, input().split())
    
    
    n, k, t = read_ints()
    
    valid_pairs = []
    pair_values = {}
    
    for i in range(k):
    	h, w, r = read_ints()
    	valid_pairs.append((h, w))
    	pair_values[(h, w)] = r
    
    valid_pairs = set(valid_pairs)
    
    varieties = [0]
    for perm in permutations(range(1, n + 1)):
    	for mask in range(0, 2 ** n):
    		mask = ('%0' + str(n) + 'd') % int(bin(mask)[2:])
    #		print mask
    		value = 0
    		for i in range(1, n + 1):
    			if mask[i - 1] == '1' and (i, perm[i - 1]) not in valid_pairs:
    				value = -10 ** 9
    			elif mask[i - 1] == '1':
    				value += pair_values[i, perm[i - 1]]
    		if value > 0:
    #			print perm
    			varieties.append(value)
    
    varieties.sort(reverse=False)
    
    #print varieties
    print varieties[t - 1]