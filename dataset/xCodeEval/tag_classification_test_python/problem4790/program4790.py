def program4790():
    n, m = map(int,input().split())
    a = []
    for i in range(n):
    	a.append(list(input()))
    s = 0
    s1 = 0
    for i in range(n):
    	count = 0
    	for j in range(m):
    		if a[i][j] == ".":
    			count += 1
    	if count == m:
    		s += m
    		s1 += 1
    for i in range(m):
    	count = 0
    	for j in range(n):
    		if a[j][i] == ".":
    			count += 1
    	if count == n:
    		s += (n - s1)
    print(s)		