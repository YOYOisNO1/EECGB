    import sys
    from math import factorial
    
    input = sys.stdin.readline
    
def A(n, k):
    	return factorial(n)//factorial(n-k)
    
def solve():
    	n, mod = map(int, input().split())
    	if n == 1:
    		print(0)
    		return
    	z = [1]
    	aaa = 0
    	for i in range(2,n+1):
    		nz = [0]*(i*i//2)
    		for j in range(len(z)):
    			for k in range(i):
    				if z[j] > 0:
    					#print(i-k+j, j, i-k-1)
    					nz[i-k-1+j] += z[j]
    		bbb = 0
    		d = [0]*(len(z)+1)
    		for w in range(len(z)-1, -1, -1):
    			d[w] = (d[w+1] + z[w]) % mod
    		e = [0]*(len(d)+1)
    		f = [0]*(len(d)+1)
    		for w in range(0, len(e)-1):
    			e[w+1] = (e[w] + d[w]) % mod
    			f[w+1] = (f[w] - w * d[w]) % mod
    		for jj in range(len(z)):
    			ccc = 0
    			#for w in range(min(len(z)-1, i+jj), jj + 1, -1):
    			#	ccc = (ccc + d[w] * (i+1+jj)) % mod
    			L = jj + 2
    			R = min(len(z)-1, i+jj)
    			#for w in range(min(len(z)-1, i+jj), jj + 1, -1):
    			#	ccc = (ccc - w * d[w]) % mod
    			if R >= L:
    				ccc = (ccc + (e[R+1] - e[L]) * (i+1+jj) \
    					+ (f[R+1] - f[L])) % mod
    			bbb = (bbb + ccc * z[jj]) % mod
    		#print(bbb)
    		aaa += (bbb * A(n,n-i)) % mod
    		#print(nz)
    		z = nz
    	#print(z)
    	print(aaa % mod)
    
    solve()