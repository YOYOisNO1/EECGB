def program2080():
    n, k, d = [int(i) for i in input().split()]
    b = [0]*(n+1)
    b[0] = 1
    b[1] = 1
    MOD = 1000000007
    for i in range(2,n+1):
    	for j in range(1,min(k+1, i+1)):
    		b[i] = (b[i] + (b[i-j]))%MOD
    a = [0]*(n+1)
    a[0] = 1
    if d != 1:
    	a[1] = 1
    for i in range(2, n+1):
    	for j in range(1, min(k+1, i+1, d)):
    		a[i] = (a[i] + a[i-j])%MOD
    print((b[n]) - a[n])%MOD