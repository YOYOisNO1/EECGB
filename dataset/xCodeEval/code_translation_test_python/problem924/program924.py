def program924():
    n, count = int(input()), 0
    while n > 0:
    	nList = [int(i) for i in str(n)]
    	n -= max(nList)
    	count += 1
    
    print(count)