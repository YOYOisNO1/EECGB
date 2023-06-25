def program1577():
    import math
    n = int(input())
    
    s = 0
    for i in range(1, n + 1):
    	k = 1
    	for j in range(i):
    		k = k * 2
    	s += k
    print(s)