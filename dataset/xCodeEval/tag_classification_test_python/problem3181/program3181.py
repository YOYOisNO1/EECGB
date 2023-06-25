def program3181():
    a = list(map(int, input().split()))
    s = sum(a)
    m = s
    
    for x in a:
    	n = a.count(x)
    	if n > 1 and s - x * min(3, n) < m:
    		m = s - x * min(3, n)
    
    print(m)