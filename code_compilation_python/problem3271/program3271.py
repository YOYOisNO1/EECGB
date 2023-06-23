def program3271():
    c = 3
    n = int(input())
    for i in range(n):
        a = int(input())
    	if a == c:
    	    print('NO')
    		exit()
        c = 6-c-a
    print('YES')