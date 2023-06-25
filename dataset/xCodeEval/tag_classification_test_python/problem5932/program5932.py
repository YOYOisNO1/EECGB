def gcd(a, b):
    	a1, b1 = a, b
    	while b1 != 0:
    		a1, b1 = b1, a1 % b1
    	return a1
    
    if __name__ == '__main__':
    	n, = map(int, input().split())
    	crush = list(map(lambda x:int(x)-1, input().split()))
    	cycle = set()
    	fail = False
    	for i in range(n):
    		cyclen = 1
    		curr = crush[i]
    		while (cyclen < n+1 and curr != i):
    			curr = crush[curr]
    			cyclen += 1
    		if curr != i:
    			fail = True
    			break
    		t = cyclen
    		if cyclen % 2 == 0:
    			t //= 2
    		cycle.add(t)
    	#print(cycle)
    	if fail:
    		print(-1)
    	else:
    		res = 1
    		for t in cycle:
    			if res % t != 0:
    				res //= gcd(res, t)
    				res *= t
    		print(res)