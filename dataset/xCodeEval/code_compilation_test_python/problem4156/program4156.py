def program4156():
    #!/usr/bin/python
    import math, random, re, sys
    while True:
    	s = sys.stdin.readline ().strip ()
    	if s == '':
    		s = sys.stdin.readline ().strip ()
    		if s == '':
    			break
    	x, y, z, k = [int (x) for x in s.split ()]
    	a, b, c = 1, 1, 1
    	i = 0
    	while i < k:
    		if a == x and b == y and c == z:
    			break
    		if a <= b and a <= c and a < x:
    			a += 1
    			i += 1
    			if i == k:
    				break
    		if b <= a and b <= c and b < y:
    			b += 1
    			i += 1
    			if i == k:
    				break
    		if c <= a and c <= b and c < z:
    			c += 1
    			i += 1
    			if i == k:
    				break
    	print a * b * c