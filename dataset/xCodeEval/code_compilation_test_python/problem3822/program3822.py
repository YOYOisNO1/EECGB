    import sys
    from math import *
    
def minp():
    	return sys.stdin.readline().strip()
    
    n = int(minp())
    m = [None]*n
    k = [None]*n
    s = [None]*n
    l = [None]*n
    dp = [None]*3
    dp[0] = [None]*(n*n)
    dp[1] = [None]*(n*n)
    dp[2] = [None]*(n*n)
    path = [None]*(n*n)
    for i in range(n):
    	m[i] = list(map(int, minp().split()))
    	kk = [None]*n
    	ss = [None]*n
    	ll = [None]*n
    	for j in range(n):
    		path[m[i][j]-1] = (i,j)
    		kkk = [None]*n
    		sss = [None]*n
    		lll = [None]*n
    		for w in range(n):
    			kkk[w] = [None]*n
    			sss[w] = [None]*n
    			lll[w] = [None]*n
    		kk[j] = kkk
    		ss[j] = sss
    		ll[j] = lll
    	k[i] = kk
    	s[i] = ss
    	l[i] = ll
    
    q = [0]*(3*n*n)
    qr = 0
    km = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
    sm = [(1,1),(1,-1),(-1,1),(-1,-1)]
    lm = [(0,1),(0,-1),(-1,0),(1,0)]
    for i in range(n):
    	for j in range(n):
    		ql = 0
    		qr = 1
    		q[0] = (i, j)
    		kc = k[i][j]
    		kc[i][j] = 0
    		while ql < qr:
    			z = q[ql]
    			d = kc[z[0]][z[1]]
    			ql += 1
    			for w in km:
    				xx,yy = w[0]+z[0],w[1]+z[1]
    				if xx >= 0 and xx < n and yy >= 0 and yy < n:
    					if kc[xx][yy] == None:
    						kc[xx][yy] = d+1
    						q[qr] = (xx,yy)
    						qr += 1
    		#print(kc)
    		ql = 0
    		qr = 1
    		q[0] = (i, j)
    		kc = s[i][j]
    		kc[i][j] = 0
    		while ql < qr:
    			z = q[ql]
    			d = kc[z[0]][z[1]]
    			ql += 1
    			for w in sm:
    				xx,yy = z[0],z[1]
    				while True:
    					xx += w[0]
    					yy += w[1]
    					if xx >= 0 and xx < n and yy >= 0 and yy < n:
    						if kc[xx][yy] == None:
    							kc[xx][yy] = d+1
    							q[qr] = (xx,yy)
    							qr += 1
    					else:
    						break
    		#print(kc)
    		ql = 0
    		qr = 1
    		q[0] = (i, j)
    		kc = l[i][j]
    		kc[i][j] = 0
    		while ql < qr:
    			z = q[ql]
    			d = kc[z[0]][z[1]]
    			ql += 1
    			for w in lm:
    				xx,yy = z[0],z[1]
    				while True:
    					xx += w[0]
    					yy += w[1]
    					if xx >= 0 and xx < n and yy >= 0 and yy < n:
    						if kc[xx][yy] == None:
    							kc[xx][yy] = d+1
    							q[qr] = (xx,yy)
    							qr += 1
    					else:
    						break
    		#print(kc)
    dp[0][0] = (0,0)
    dp[1][0] = (0,0)
    dp[2][0] = (0,0)
    for i in range(0,n*n-1):
    	x,y = path[i]
    	xx,yy = path[i+1]
    	for z in range(3):
    		if z == 0:
    			w = k
    		elif z == 1:
    			w = s
    		else:
    			w = l
    		dist = w[x][y][xx][yy]
    		if dist != None:
    			for j in range(3):
    				if dp[j][i] != None:
    					if j == z:
    						nd = (dp[j][i][0]+dist,dp[j][i][1])
    					else:
    						nd = (dp[j][i][0]+dist+1,dp[j][i][1]+1)
    					if dp[z][i+1] == None:
    						dp[z][i+1] = nd
    					else:
    						dp[z][i+1] = min(dp[z][i+1],nd)
    for j in range(n*n-1,n*n):
    	qq = [dp[i][j] if dp[i][j] != None else (100000,0) for i in range(3)]
    	qm = min(qq)
    	#print(j,qm)
    	print(qm[0], qm[1])