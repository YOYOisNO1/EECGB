def program1960():
    
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    s = 0
    for i in range(n):
    	if a[i] > 8:
    		s += 8
    	else:
    		s += a[i]
    	if s >= k:
    		print(i+1)
    		break
    if s < k:
    	print(-1)
    else
    	print(n)