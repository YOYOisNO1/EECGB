def program2056():
    n,k,d = input().split()
    n = int(n)
    k = int(k)
    d = int(d)
    c = [0]*(n+1)
    fs = [0]*(n+1)
    fs[0] = 0
    c[0] = 1
    for i in range(1,n+1):
    	for j in range(1,min(n,k)+1):
    		fs[i] += fs[i-j]
    		if(j<d):
    			c[i] +=c[i-j]
    		else:
    			fs[i] += c[i-j]
    print(fs[n]%1000000007)