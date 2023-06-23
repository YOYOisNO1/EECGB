    import math
def isLucky(num):
    	s = str(num)
    	for i in s:
    		if i != '4' and i != '7':
    			return False
    	return True
    
def getLucky(d):
    	if d == 1:
    		for i in [4, 7]:
    			yield str(i)
    	else:
    		l = [i for i in getLucky(d-1)]
    		for j in l:
    			yield '4'+j
    		for j in l:
    			yield '7'+j
    
    luckies = []
    for d in range(1,11):
    	for i in getLucky(d):
    		luckies.append(int(i))
    
def canto(l, k):
    	# find the k(th) permutation of list l, k counts from 1
    	n = len(l)
    	p = k - 1
    	a = []
    	i = n - 1
    	mark = [False]*(n+1)
    	while len(a) < n:
    		fac = math.factorial(i)
    
    		a.append(p/fac)
    		p %= fac
    		i -= 1
    		j = 1
    		cnt = 0
    		while cnt < a[-1]+1:
    			if not mark[j]:
    				cnt += 1
    			j += 1
    		a[-1] = j-1
    		mark[a[-1]] = True
    	return [l[i-1] for i in a]
    
    n, k = map(int, input().split())
    
    for tail in range(1, n+1):
    	fac = math.factorial(tail)
    	if fac >= k:
    		break
    l = [i for i in range(n+1-tail, n+1)]
    p_tail = canto(l, k)
    # print 'tail',tail
    # print p_tail
    
    ans = 0
    for lucky in luckies:
    	if lucky > n: break
    	# print 'lucky is',lucky
    	if lucky <= n-tail:
    		ans += 1
    		# print lucky
    	else:
    		i = p_tail.index(lucky)
    		if isLucky(n-tail+1+i):
    			ans += 1
    			# print lucky
    print ans