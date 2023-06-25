def program5568():
    n, m = map(int, input().split())
    a = n%m
    for i in range(m):
    	if i<m-a:
    		print(n//m, end = ' ')
    	else:
    		print(n//m+1, end = ' ')