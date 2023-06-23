def program3814():
    q = int(input())
    import numpy as np
    for i in range(q):
    	a, b, m = list(map(int,input().split()))
    	l = a + 1 
    	r = a + m
    	c = 0
    	poziom = 0
    	while True:
    		if l > b:
    			print(-1)
    			break
    		if b <= r and b >= l:
    			c = 1
    			last = [l, r]
    			break
    		poziom += 1
    		l *= 2
    		r *= 2
    	if c == 1:
    		mat = [(a + 1) * 2 ** i for i in range(poziom + 1)]
    		sumka = a
    		for i in range(poziom + 1):
    			if mat[-1] == b:
    				break
    			else:
    				pom = min(sumka + m - mat[i], (b - mat[-1]) // (2 ** (poziom - i)))
    				sumka += mat[i]
    				for j in range(i, poziom + 1):
    					mat[j] += pom * 2 ** (j - i)
    		print(len(mat) + 1, end = " ")
    		print(a, end =  " ")
    		for i in range(len(mat)):
    			if i < len(mat) - 1:
    				print(mat[i], end = " ")
    			else:
    				print(mat[i], end = "\n")
    			
    		