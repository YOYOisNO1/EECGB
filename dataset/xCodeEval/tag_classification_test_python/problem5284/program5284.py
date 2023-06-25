    import math
    from collections import deque
def p(mid, arr, k):
    	counter = 0
    	#d = deque()
    	totalSum = 0
    	#sliding window
    	#print((arr))
    	size = 0
    	for i in range(a, b+1):
    		size += 1
    		#d.append(arr[i])
    		
    		totalSum += arr[i]
    		takeAway = 0
    		if size > mid:
    			takeAway = arr[i - mid]
    
    		totalSum -= takeAway
    
    		if size >= mid:
    			if totalSum < k:
    				return False
    
    
    
    	if totalSum < k:
    		return False
    	return True
    
    
    
    splitted = input().split(" ")
    a = int(splitted[0])
    b = int(splitted[1])
    k = int(splitted[2])
    
    #generate primes up to b, using sieve
    sieve = [True] * (b + 1)
    primes = deque()
    for i in range(2, b + 1):
    	#print((i))
    	if sieve[i]:
    		primes.append(i)
    	else:
    		continue
    	j = 2 * i
    	while j < b + 1:
    		sieve[j] = False
    		j += i
    
    arr = [0] * (b + 1)
    for prime in primes:
    	arr[prime] = 1
    #print((primes))
    #print((arr))
    counter = 0
    savedI = -1
    low = 1
    high = b - a + 1
    while low + 1 < high:
    	mid = low + (high - low)/2
    	#print((str(low)) + ", " + str(high))
    	if p(mid, arr, k) == True:
    		high = mid
    		#print((str(mid)) + " returned true")
    	else:
    		low = mid
    		#print((str(mid)) + " returned false")
    if p(high, arr, k) == True:
    	print((high))
    else:
    	print((-1))