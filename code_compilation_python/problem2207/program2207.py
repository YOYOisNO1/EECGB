def program2207():
    n, m = map(int, input().strip().split())
    l = map(int, input().strip().split())
    
    a = [0] * (n)
    rev_a = {}
    flag = 0
    
    for i in xrange(len(l) - 1):
    	key = l[i]
    	val = l[i + 1] - l[i]
    	val = val if val > 0 else val + n
    	if rev_a.get(val) and rev_a.get(val) != key:
    		flag = 1
    		break
    	else:
    		a[key - 1] = val
    		rev_a[val] = key
    
    if flag:
    	print -1
    else:
    	last_unchecked = 1
    	for i in xrange(n):
    		if not a[i]:
    			while last_unchecked in rev_a:
    				last_unchecked += 1
    			a[i] = last_unchecked
    			last_unchecked += 1
    	print " ".join(map(str, a))