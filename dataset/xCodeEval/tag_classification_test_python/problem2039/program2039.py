    ###############################################################################
    #Imports
    import collections
    import itertools
    from functools import lru_cache
    import sys
    import math
    ###############################################################################
    #Constants
    MOD = int(1e9)+7
    ###############################################################################
    #Helper
def helper():
    	pass
    ###############################################################################
    #Solver
def solve():
    	n, k, d = map(int, input().split(' '))
    	@lru_cache(None)
	def dfs(score, pred):
    		if score == 0:
    			return 1 if pred else 0
    		elif score < 0:
    			return 0
    		else:
    			ans = 0
    			for i in range(1, k + 1):
    				if score - i >= 0:
    					if i>=d:
    						ans = ((ans % MOD) + \
    							(dfs(score - i, True) % MOD)) % MOD
    					else:
    						ans = ((ans % MOD) + \
    							(dfs(score - i, pred) % MOD)) % MOD
    				else:
    					break
    			return ans
    	print(dfs(n,False))
    
    ###############################################################################
    #Driver
    t = 1
    for _ in range(t):
    	solve()
    ###############################################################################