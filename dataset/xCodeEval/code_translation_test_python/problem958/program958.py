    from math import ceil, log, floor, sqrt
    import math	
    	
def mod_expo(n, p, m):
    	"""find (n^p)%m"""
    	result = 1
    	while p != 0:
    		if p%2 == 1:
    			result = (result * n)%m
    		p //= 2
    		n = (n * n)%m
    	return result
    	
def find_k(x, y, n):
    	return ((n-y)//x)*x + y
    
def count_sticks(n):
    	if n%2 == 0:
    		return n//2
    	return n//2 +1 
    
def get_types(n, r):
    	if r < n:
    		return (r*(r+1))//2
    	r = n-1
    	return (r*(r+1))//2 + 1
    	
def happy_guests(a, b, n, m):
    	mn = min(n, m)
    	a -= mn
    	b -= mn
    	n -= mn
    	m -= mn
    	if a < 0 or b < 0:
    		return False
    	if n > 0:
    		return a+b >= n
    	return min(a, b) >= m 	
    	
def find_max_len(s):
    	n = len(s)
    	l, r = 0, n-1
    	count = n
    	while l < r and s[l] == 'a':
    		l += 1
    	while r > l and s[r] == 'a':
    		r -= 1
    	for i in range(l, r+1):
    		if s[i] != 'b':
    			count -= 1
    	return count
    	
def is_rectangle(a, b, c):
    	for i in range(2):
    		if a[i] == b[i]:
    			idx = (i+1)%2
    			if c[idx] >= max(a[idx], b[idx]) or c[idx] <= min(a[idx], b[idx]): 
    				return True
    		if b[i] == c[i]:
    			idx = (i+1)%2
    			if a[idx] >= max(b[idx], c[idx]) or a[idx] <= min(b[idx], c[idx]):
    				return True
    		if a[i] == c[i]:
    			idx = (i+1)%2
    			if b[idx] >= max(a[idx], c[idx]) or b[idx] <= min(a[idx], c[idx]):
    				return True
    	return False
    	
def count_lines(points):
    	mpx, mpy = {}, {}
    	for point in points:
    		if point[0] not in mpx:
    			mpx[point[0]] = 1
    		else:
    			mpx[point[0]] += 1
    		if point[1] not in mpy:
    			mpy[point[1]] = 1
    		else:
    			mpy[point[1]] += 1
    	#print(len(mpx), len(mpy))
    	#print(mpx, mpy)
    	if len(mpx) == 1 or len(mpy) == 1:
    		return 1
    	if is_rectangle(points[0], points[1], points[2]):
    		return 2
    	if is_rectangle(points[0], points[2], points[1]): 
    		return 2
    	if is_rectangle(points[2], points[1], points[0]):
    		return 2	
    	return 3	
    	
    t = 1
    #t = int(input())
    while t:
    	t = t - 1
    	points = []
    	#n = int(input()) 
    	#n, k = map(int, input().split()) 
    	# = map(int, input().split())
    	#arr = list(map(int, input().strip().split()))[:n]
    	#w = list(map(int, input().strip().split()))[:k]
    	for i in range(3):
    		x, y = map(int, input().split()) 
    		points.append((x, y))
    	#s = input()
    	#if happy_guests(a, b, n, m):
    #		print("Yes")
    #	else:
    #		print("No")
    	
    	#print(get_res(s))
    	print(count_lines(points))