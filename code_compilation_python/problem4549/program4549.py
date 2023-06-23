def do(i):
    	if i == "(":
    		return 1
    	else:
    		return -1
def find(i,idx):
    	if i<n-idx:
    		return idx+i+1
    	else:
    		return i-(n-idx)+1
    n = input()
    arr = map(do,input())
    s = [0]*n
    s[n-1] = arr[n-1]
    maxi = 0
    maxv = 0
    for i in range(n-1)[::-1]:
    	s[i] = s[i+1] + arr[i]
    	if s[i] > maxv:
    		maxv = s[i]
    		maxvi = i
    newv = arr[maxvi:]+arr[:maxvi]
    print " ".join(["(" if i == 1 else")" for i in newv ])
    
    if sum(newv) != 0:
    	print 0
    	print 1,1
    else:
    	cnt = 0
    	cnt1 = -1
    	maxv = 0
    	l = 0
    	r = 0
    	last = 0
    	st = 0
    	for i in range(n):
    		st += newv[i]
    		if st == 0:
    			cnt += 1
    			cnt1 = -1
    			last = i+1
    		elif st == 1:
    			cnt1 += 1
    			if cnt1 > maxv:
    				maxv = cnt1
    				l = last
    				r = i+1
    	if maxv > cnt:
    		print maxv+1
    		print find(l,maxvi),find(r,maxvi)
    	else:
    		print cnt,1,1