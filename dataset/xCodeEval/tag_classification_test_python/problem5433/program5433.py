    from sys import stdin
    input = lambda: stdin.readline().rstrip()
    input = lambda: int(input())
    I=lambda: map(int, input().split())
    
    M = 1000000007
    
    FACTS = [1]
    cur = 1
    for i in xrange(1, 200001):
    	cur = (cur*i)%M
    	FACTS.append(cur)
    	
def modExp(a, exp, mod):
    	assert not (a == 0 and exp == 0)
    	if a == 0:
    		return 0
    	res = 1
    	while exp > 0:
    		if exp%2 == 1:
    			res = (res * a) % mod
    			exp -= 1
    		elif exp%2 == 0:
    			a = (a*a)%mod
    			exp = exp//2
    	return res
    	
# def getBezout(a, b): #ax + by = gcd(a, b)
    	# r1, r2 = a, b
    	# s1, s2 = 1, 0
    	# t1, t2 = 0, 1
    	# q = 0
    	# while r2 != 0:
    		# q = r1//r2
    		# s1, s2 = s2, s1 - q*s2
    		# t1, t2 = t2, t1 - q*t2
    		# r1, r2 = r2, r1%r2
    	# x = s1
    	# y = t1
    	# return x, y
    	
# def modInv(a, m): #gcd(a, m) == 1
    	# return getBezout(a, m)[0]
    	
# def chooseMod(n, k, m):
    	# if k > n or k < 0:
    		# return 0
    	# if k == 0 or k == n:
    		# return 1
    	# if k > n//2:
    		# return chooseMod(n, n-k, m)
    	# res = FACTSN[k]
    	# q = FACTS[k]
    	# qn = modInv(q, m)
    	# return (res*qn)%M
    
# def pickEven(n, m):
    	# r = 0
    	# for i in xrange(0, n+1, 2):
    		# r = (chooseMod(n, i, m)+r)%m
    	# return r
    
    t = input()
    for _ in xrange(t):
    	n,k = I()
    	FACTSN = [0]
    	cur = 1
    	for i in xrange(n, 0, -1):
    		cur = (cur*i)%M
    		FACTSN.append(cur)
    	# evenN = pickEven(n, M)
    	curDp = 1
    	if n%2==1:
    		evenN = modExp(2, n-1, M)
    		for i in xrange(1, k+1):
    			curDp = (curDp*(1+evenN))%M
    	else:
    		evenN = modExp(2, n-1, M)
    		TWOSEXP = [1]
    		q2 = modExp(2, n, M)
    		cur = 1
    		for i in xrange(k):
    			cur = (cur*q2)%M
    			TWOSEXP.append(cur)
    		for i in xrange(1, k+1):
    			curDp = ((curDp*(evenN-1))%M + TWOSEXP[i-1])%M
    	print(curDp)