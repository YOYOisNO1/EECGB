    #!/usr/bin/env python3
    #
    # NC113552 - Steps to One
    #
    import sys, os, math, re, time, random, copy, shutil, itertools, functools, heapq
    from bisect import bisect_left, bisect_right
    from collections import deque, defaultdict, Counter, OrderedDict
    
    MOD = int(1e9 + 7)
    
def gcd(a, b):
    	while b: a, b = b, a % b
    	return a
    
def mpow(x, n):
    	r = 1
    	while n > 0:
    		if n & 1 == 1: r = r * x % MOD
    		x, n = x * x % MOD, n >> 1
    	return r
    
    m = int(input())
    
    d = [[] for _ in range(m + 1)]
    for i in range(1, m + 1):
    	for j in range(i + i, m + 1, i):
    		d[j].append(i)
    
    pr = [False, False] + [True] * (m - 1)
    fa = [{} for _ in range(m + 1)]
    for i in range(2, m + 1):
    	if not pr[i]: continue
    	for j in range(i, m + 1, i):
    		pr[j] = False
    		k, c = j, 0
    		while k % i == 0:
    			k, c = k // i, c + 1
    		fa[j][i] = c
    
def calc(g, x):
    	p = []
    	for k, v in fa[x].items():
    		if k not in fa[g]:
    			p.append(k)
    		elif fa[g][k] != v:
    			p.append(k)
    	sz = len(p)
    	n = m // g
    	ret = m // g
    	for i in range(1, 1 << sz):
    		sign = z = 1
    		for j in range(sz):
    			if (i & (1 << j)) != 0:
    				z *= p[j]
    				sign *= -1
    		ret += sign * (n // z)
    	return ret
    
    dp = [0] * (m + 1)
    
    mm = mpow(m, MOD - 2)
    for i in range(2, m + 1):
    	r = 1
    	for x in d[i]:
    		c = calc(x, i)
    		r = (r + dp[x] * c % MOD * mm % MOD) % MOD
    	c = m // i
    	dp[i] = r * m % MOD * mpow(m - c, MOD - 2) % MOD
    
    ans = 1
    for i in range(1, m + 1):
    	ans = (ans + dp[i] * mm % MOD) % MOD
    
    print(ans)
    
    	    	         				  			 	   		