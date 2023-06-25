    n = int(input())
    s = list(input())
    L = 1
    R = 1
def check():
    	calc = 0
    	min = 0
    	cntmin = 0
    	for ch in s:
    		if ch == '(':	calc += 1
    		else:	calc -= 1
    		if min > calc:
    			min = calc
    			cntmin = 1
    		elif min == calc:
    			cntmin += 1
    	return cntmin if calc == 0 else 0
     
    best = check()
    for i in range(n):
    	for j in range(i + 1, n, 1):
    		s[i], s[j] = s[j], s[i]
    		new = check()
    		s[j], s[i] = s[i], s[j]
    		if (new > best):
    			best = new; L = 1+i; R = 1+j
    print(best)
    print(L, R)