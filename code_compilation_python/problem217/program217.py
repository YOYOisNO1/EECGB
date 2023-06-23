def program217():
    n = input()
    n = int(n)
    k = 0
    for i in range(1, n + 1):
    	for j in range(1, (n // 2) + 1 + (n % 2)):
    		if (i + j) % (n + 1) == 1:
    			k += 1
    print (k)