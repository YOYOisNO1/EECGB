def program4887():
    n, k = map(int, input().split())
    a = []
    for i in range(1,n+1):
    	if i*i > n:
    		break
    	if n % i == 0:
    		a.append(i)
    		if i*i != n:
    			a.append(n//i)
    a.sort()
    if k-1 < len(a):
    	print(a[k-1])
    else:
    	print(-1)
    