def program15():
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    a.sort()
    
    v = 0
    for i in range(n-1):
    	v += a[i]
    	if v > m:
    		print('NO')
    		break
    else:
    	print('YES')