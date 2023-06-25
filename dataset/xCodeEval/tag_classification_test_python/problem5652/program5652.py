    #!/usr/bin/python
    
    import sys
    from math import *
    
def Nil(): return map(int, sys.stdin.readline().split())
    
    n, m = Nil()
    
def nhp7(n):
    	""" next higher power of 7 """
    	p = 1
    	c = 0
    	while p < n:
    		p *= 7
    		c += 1
    	return max(1, c)
    
    if n >= 7**7 or m >= 7**7:
    	print(0)
    	sys.exit()
    
def makeindex(n):
    	"""
    	Return index of subset of digits to how many numbers less
    	than n can be formed with these digits.
    	"""
    	assert n <= 7**7
    	
    	n7 = nhp7(n)
    	hindex = [0] * 2**7
    	for v in range(n):
    		have = 0
    		skip = False
    		ndigits = 0
    		while ndigits < n7:
    			d = v % 7
    			bv = (1<<d)
    			if have & bv != 0:	# digit already used
    				skip = True
    				break
    			ndigits += 1
    			have |= bv
    			v /= 7
    
    		if skip:
    			continue
    
    		hindex[have] += 1
    
    	return hindex
    
    hn = makeindex(n)
    hm = makeindex(m)
    
    #
    # Multiply all feasible sets of digits that can appear
    # in the hours with the subsets of complementary digits in the
    # minutes.
    #
    answer = 0
    for have in range(2**7):
    	if hn[have] == 0:
    		continue
    
    	havenot = ((1<<7) - 1) ^ have
    	answer += hn[have] * sum(hm[ss] for ss in range(2**7) if (ss & havenot) == ss)
    
    print(answer)
    