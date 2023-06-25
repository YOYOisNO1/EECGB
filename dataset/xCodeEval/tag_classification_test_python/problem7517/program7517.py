def program7517():
    n, ts = int(input()), sorted(map(int, input().split()))
    t, m = int(input()), 1
    for i in range(n):
    	for j in range(i + 1, n):
    		dt = ts[j] - ts[i]
    		if dt > t:
    			break
    		else:
    			m = max(m, j - i + 1)
    print(m)