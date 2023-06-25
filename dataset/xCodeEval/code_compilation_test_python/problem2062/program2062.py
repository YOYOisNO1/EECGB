def program2062():
    import sys
    n,k = map(int, sys.stdin.readline().split())
    s = input()
    g = -1
    t = -1
    for i in range(len(s)):
    	if s[i] == 'G':
    		g = i
    	if s[i] == 'T'
    		t = i
    
    if t > g:
    	t,g = g,t
    
    cur = t
    found = False
    while cur < n:
    	if cur == g:
    		found = True
    		break
    	if s[cur] == '#':
    		break
    	cur += k
    if found:
    	print 'YES'
    else:
    	print 'NO'