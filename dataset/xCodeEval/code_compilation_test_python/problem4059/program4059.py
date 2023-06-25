def main():
    	(n, q) = (int(x) for x in input().split())
    	L = [None] * q
    	for i in range(q):
    		(a, b) = (int(x) for x in input().split())
    		L[i] = (a, b)
    	print(solver(n, L))
    
def solver(n, L):
    	count = 0
    	for (a, b) in L:
    		if b == 'a':
    			count += helper(n - 2, L, a[0])
    	return count
    
def helper(n, L, last):
    	if n == 0:
    		return 1
    	else:
    		count = 0
    		for (a, b) in L:
    			if b == last:
    				count += helper(n - 1, L, a[0])
    		return count
    
    # L = [('ab', 'a'), ('cc', 'c'), ('ca', 'a'), ('ee', 'c'),
    # ('ff', 'd')]
    # L2 = [('bb', 'a'), ('ba', 'a')]
    # print(solver(6, L2))
    main()