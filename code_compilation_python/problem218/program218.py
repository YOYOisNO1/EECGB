def program218():
    n = int(input())
    s = set()
    for k in range(1,n+1):
    	s.add(k)
    c = True
    prev = 1
    s.remove(1)
    res = 0
    while len(s) != 0:
    	if c == True:
    		m = max(s)
    	else:
    		m = min(s)
    	s.remove(m)
    	res += (prev + m) % (n+1)
    	c = not c
    	prev = m
    print(res)