def max(a, b):
    	if a > b:
    		return a
    	return b 
    
    n = int(input())
    a = list(map(int, input().split())) 
    
    pos1 = 0, posn = 0
    
    for i in range(n):
    	if a[i] == 1:
    		pos1 = i
    	if a[i] == n:
    		posn = i
    
    print(max(pos1, max(n - 1 - pos1, max(posn, n - 1 - posn))))