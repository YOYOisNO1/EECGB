def program4409():
    n, m, k = input().spilt(' ')
    n = int(n)
    m = int(m)
    k = int(k)
    if k > n:
    	print(pow(m, n, 1000000007))
    elif k == 1:
    	print(pow(m, n, 1000000007))
    else:
    	if k & 1:
    		print(m * m)
    	else:
    		print(m)