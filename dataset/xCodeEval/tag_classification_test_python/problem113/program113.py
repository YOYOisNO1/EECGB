def program113():
    n, h, m = map(int, input().split())
    arr = [h]*n
    for i in range(m):
    	l, r, x = map(int, input().split())
    	for j in range(l-1, r):
    		arr[j] = min(arr[j], x)
    	
    
    su = 0
    for x in arr:
    	su += x*x
    
    print(su)