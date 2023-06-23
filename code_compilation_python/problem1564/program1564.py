def program1564():
    n,k = map(int,input().split())
    s = [[0 for i in range(8)] for j in range(8)]
    for i in range(k):
    	u,v = map(int,input().split())
    	s[u][v] = 1
    	s[v][u] = 1
    if(n <= 6 or k == 0):
    	print(k)
    else:
    	m = 10
    	for i in range(1,8):
    		s1 = sum(s[i])
    		if(s1 < m):
    			m = s1
    	a = [[0,0,0]]
    	for i in range(1,8):
    		if(sum(s[i]) == m ):
    			f = i
    		for j in range(1,8):
    			if(f == j):
    				continue
    			ct = 0
    			for k in range(1,8):
    				if s[f][k] != s[j][k]:
    					ct += 1
    			if s[j][f] == 1:
    				ct -= 1
    			#print(j,f,ct)
    			a.append([ct,j,f])
    	a.sort()
    	ind1 = a[-1][1]
    	ind2 = a[-1][2]
    	sum = sum1 = 0
    	#print(ct,ind1,ind2)
    	#print(s[ind1],s[ind2])
    	for i in range(1,8):
    		if(s[ind1][i] == 1 and s[ind2][i] == 1):
    			sum1 += 1
    	for i in range(1,8):
    		if i == ind1 or i == ind2:
    			continue
    		for j in range(1,8):
    			if j == ind1 or j == ind2:
    				continue
    			sum += s[i][j]
    	print(a[-1][0]+sum1+(sum//2))