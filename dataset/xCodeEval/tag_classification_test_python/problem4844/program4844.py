    from math import ceil, log, floor, sqrt
    import math	
    	
    	
    k = 1	
def mod_expo(n, p, m):
    	"""find (n^p)%m"""
    	result = 1
    	while p != 0:
    		if p%2 == 1:
    			result = (result * n)%m
    		p //= 2
    		n = (n * n)%m
    	return result
    	
def is_prime(n):
    	m = 2
    	while m*m <= n:
    		if n%m == 0:
    			return False
    		m += 1
    	return True
    	
def find_sum(n, a):
    	a.insert(0, 0)
    	for i in range(1, n+1):
    		prev = a[i] & a[i-1]
    		cur = a[i] | a[i-1]
    		a[i-1] = prev
    		a[i] = cur
    	return sum(m*m for m in a)
    
def prin_abc(x, y, z):
    	l = [x, y, z]
    	l.sort()
    	if l[1] < l[2]:
    		print("NO")
    		return 
    	a = b = l[0]
    	c = l[2]
    	print("YES")
    	print(a, b, c)
    	
def get_scores(n, vals):
    	l = 0
    	r = n-1
    	turn = 0
    	sereja = 0
    	dima = 0
    	while l <= r:
    		if vals[l] > vals[r]:
    			cur = vals[l]
    			l += 1
    		else:
    			cur = vals[r]
    			r -= 1
    		if turn == 0:
    			sereja += cur
    		else:
    			dima += cur
    		turn = not turn
    	print(sereja, dima)
    		
def count_lamps(n, m):
    	return (n*m + 1)//2
    	
def find_holidays(n):
    	cnt = 2*(n//7)
    	rem = n%7
    	#if n < 7:
    	#	print(0, cnt)
    	mx = mn = cnt
    	if rem == 1:
    		mx += 1
    	elif rem > 1:
    		mx += 2
    	if rem == 6:
    		mn += 1
    	
    	print(mn, mx)
    	
def get_cnt(n, S):
    	cnt = 0
    	while S:
    		cnt += (S//n)
    		S -= (S//n)*n
    		n = S
    	return cnt
    		
    t = 1
    #t = int(input())
    while t:
    	t = t - 1
    	k, g = 0, 0
    	points = []
    	#n = int(input()) 
    	#a = input()
    	#b = input()
    	#s, v1, v2, t1, t2 = map(int, input().split()) 
    	n, S  = map(int, input().split()) 
    	#print(discover())
    	# = map(int, input().split())
    	#a = list(map(int, input().strip().split()))[:n]
    	#w = list(map(int, input().strip().split()))[:k]
    	#for i in range(3):
    	#	x, y = map(int, input().split()) 
    	#	points.append((x, y))
    	#s = input()
    	#if sasha_wins(n, k):
    	#	print("YES")
    	#else:
    	#	print("NO")
    	#get_cnt(a,  b);
    	print(get_cnt(n, S))