def program3570():
    n, t = tuple(map(int, input().strip().split()))
    q = list(input().strip())
    while t > 0:
    	i = 1
    	while i < n:
    		if q[i-1] == 'B' and q[i] == 'G':
    			q[i-1], q[i] = 'G', 'B'
    			i += 1
    		i += 1
    	t -= 1
    print("".join(q))