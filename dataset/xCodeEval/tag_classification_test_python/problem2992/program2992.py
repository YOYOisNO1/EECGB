def program2992():
    import sys
    import math
    inpu = sys.stdin.readline
    prin = sys.stdout.write
    
    m = 998244353
    n, x = map(int, input().split())
    if n >= x + 1:
    	prod = 1
    	for i in range(n):
    		prod = (prod * x) % m
    	print(prod)
    else:
    	binomial = [[0] * (n + 1) for i in range(n + 1)]
    	for i in range(n + 1):
    		for j in range(i + 1):
    			if i == j or j == 0:
    				binomial[i][j] = 1
    			else:
    				binomial[i][j] = (binomial[i - 1][j] + binomial[i - 1][j - 1]) % m
    	table = [[0] * (n + 1) for i in range(x + 1)]
    	powers = [[0] * (n + 1) for i in range(n + 1)]
    	combo = [[0] * (n + 1) for i in range(n + 1)]
    	for i in range(n + 1):
    		powers[i][0] = 1
    		for j in range(n):
    			powers[i][j + 1] = (powers[i][j] * i) % m
    	for j in range(1, n + 1):
    		for k in range(j + 1):
    			combo[j][k] = (powers[j - 1][j - k] * binomial[j][k]) % m
    	for i in range(2, n + 1):
    		table[1][i] = 1
    	for i in range(1, x + 1):
    		table[i][0] = 1
    	for i in range(2, x + 2 - n):
    		for j in range(2, n + 1):
    			if j == i + 1:
    				prod = 1
    				for k in range(j):
    					prod = (prod * i) % m
    				table[i][j] = prod
    			elif j > i:
    				table[i][j] = (table[i][j - 1] * i) % m
    			else:
    				table[i][j] = sum(table[i - j + 1][k] * combo[j][k] for k in range(j + 1)) % m
    	print(sum(table[x - n + 1][k] * combo[n][k] for k in range(n + 1)) % m)
    	#print(table)