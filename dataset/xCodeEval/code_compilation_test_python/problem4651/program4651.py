    #! /usr/bin/python
    
    from collections import deque
    
def gcd(a, b):
    	return a if b == 0 else gcd(b, a % b)
    
    m, a, b = [int(inp) for inp in input().split()]
    
    m0 = min(a + b - 1, m)
    
    canGet = [1 if i == 0 else 0 for i in xrange(m0 + 1)]
    count = 1
    total = 1
    q = deque()
    for x in xrange(1, m0 + 1):
    	if x - a >= 0 and canGet[x - a] == 1:
    		canGet[x] = 1
    		count += 1
    		q.append(x)
    		while len(q) > 0:
    			j = q.pop()
    			if j + a <= x and canGet[j + a] == 0:
    				canGet[j + a] = 1
    				count += 1
    				q.append(j + a)
    			if j - b >= 0 and canGet[j - b] == 0:
    				canGet[j - b] = 1
    				count += 1
    				q.append(j - b)
    	total += count
    
    g = gcd(a, b)
    
    m1 = min(m, ((m0 + g)/g)*g - 1)
    total += (m1 - m0)*count
    
    m2 = (m/g)*g - 1
    if m2 >= m1:
    	total += ((m2 - m1)/g)*g*((m1 + 1)/g + (m2 + 1)/g + 1)/2
    	total += (m - m2)*(m/g + 1)
    
    print total