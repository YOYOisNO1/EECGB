    n,m = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    
    
def esht(x, y):
    	if not (any(q in y[0] for q in x[0]) and not all(q in y[0] for q in x[0])):
    		return None
    	for q in x[0]:
    		if q in y[0]:
    			return q
    
    a = []
    for i in range(len(first)):
    	if i % 2 == 1:
    		continue
    	a.append(([first[i], first[i+1]], []))
    
    b = []
    for i in range(len(second)):
    	if i % 2 == 1:
    		continue
    	b.append(([second[i], second[i+1]], []))
    
    some = -1
    for aa in a:
    	for bb in b:
    		q = esht(aa, bb)
    		if q is not None:
    			aa[1].append(q)
    			bb[1].append(q)
    			some = q
    
def eq(lst):
    	return lst[1:] == lst[:-1]
    
    ok = True
    for aa in a:
    	for q in aa[1]:
    		if q != some:
    			ok = False
    if ok:
    	print(some)
    else:
    	ok2 = True
    	for aa in a:
    		if not eq(aa[1]):
    			ok2 = False
    	for bb in b:
    		if not eq(bb[1]):
    			ok2 = False
    	if ok2:
    		print(0)
    	else:
    		print(-1)
    			
    			