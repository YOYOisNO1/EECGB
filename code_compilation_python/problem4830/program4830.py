def program4830():
    from fractions import gcd
    
    n = int(input())
    f = [0] + map(int, input().split())
    
    max_prefix = 0
    period = 1
    
    visited = set()
    for i in xrange(1, n+1):
    	if i not in visited:
    		j, steps = i, 0
    		while j not in visited:
    			visited.add(j)
    			j = f[j]
    			steps += 1
    		k, prefix = i, 0
    		while k != j:
    			k = f[k]
    			prefix += 1
    		max_prefix = max(max_prefix, prefix)
    		loop = steps - prefix
    		if loop:
    			period = period * loop / gcd(period, loop)
    
    p = period
    while period < max_prefix:
    	period += p
    print period