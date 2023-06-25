def program3055():
    n,m = map(int, input().split())
    l = list(map(int, input().split()))
    c = 0
    i = 0
    s = 0
    while i<n:
    	while s<m:
    		s = s + l[i]
    		i = i+1
    	s = 0
    	n = n-1
    	c = c+1
    	i = i-1
    print(c)