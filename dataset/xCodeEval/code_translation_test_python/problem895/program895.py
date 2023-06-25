def program895():
    n,k =map(int,input().split())
    l = 2**n - 1
    while l/2 != k-1:
    	if l/2 < k - 1:
    		k = k - l/2 - 1
    	n -= 1
    	l = 2**n - 1
    print(n)