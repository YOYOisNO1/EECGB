def program3815():
    import sys
    sys.stdin = open('C:\\Users\\sharr\\Documents\\Input.txt', 'r')  
    sys.stdout = open('C:\\Users\\sharr\\Documents\\Output.txt', 'w') 
    
    q = int(input())
    for _ in range(q):
    	a, b, m = map(int, input().split())
    	mn = [a]
    	mx = [a]
    	sum_mn = a
    	sum_mx = a
    	ok = False
    
    	for n in range(51):
    		if mn[-1] <= b <= mx[-1]:
    			ok = True
    			break
    
    		mn.append(sum_mn + 1)
    		mx.append(sum_mx + m)
    		sum_mn += mn[-1]
    		sum_mx += mx[-1]
    
    		if mn[-1] > b:
    			break
    
    	if not ok:
    		print(-1)
    		continue
    
    	r = [0] * n
    	s = b - mn[-1]
    	for i in range(n):
    		x = s // max(1, 2 ** (n - i - 2))
    		if x > m - 1:
    			x = m - 1
    		r[i] = x + 1
    		s -= x * max(1, 2 ** (n - i - 2))
    
    	s = a
    	res = [a]
    	for i in range(n):
    		res.append(s + r[i])
    		s += res[-1]
    
    	print(len(res), *res)