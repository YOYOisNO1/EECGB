    n, k = map(int, input().split())
    a = map(int, input().split())
    s = set()
    d = dict()
    ans = 0
    
def find():
    	max = -1
    	maxx = -1
    	for i in s:
    		if len(d[i]) == 0:
    			maxx = i
    			max = n + 1
    		else:
    			if max < d[i][-1]:
    				max = d[i][-1]
    				maxx = i
    	return maxx
    
    
    for i in xrange(n + 10):
    	d[i] = []
    
    for i,x in enumerate(a):
    	d[x].append(i)
    
    for kk,v in d.items():
    	d[kk] = list(reversed(v))
    
    for i in a:
    	if not i in s:
    		ans += 1
    		if len(s) >= k:
    			x = find()
    			s.remove(x)
    
    		s.add(i)
    	d[i].pop()
    
    print(ans)