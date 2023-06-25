    import math
    # t = int(input()) 
    t = 1
    
    
def check(k, totalCandies, ate=0):
    	base = totalCandies
    	while 2*ate < base and totalCandies > 0:
    		ateNow = min(k, totalCandies)
    		ate += ateNow
    		totalCandies -= ateNow
    		totalCandies -= (totalCandies//10)
    	# print(ate, totalCandies)
    	return 2*ate >= base		
    
    # print(check(3, 68))s
    
    for _ in range(t):
    	candies = int(input())
    	l, r, store  = 1, candies, math.ceil(candies/2)
    
    	while l <= r:
    	 	mid = (l+r)//2
    	 	ateHalf = check(mid, candies)
    	 	# print(l, mid, r, "at mid", ateHalf)
    	 	if ateHalf is True:
    	 		store = mid
    	 		r = mid - 1
    	 	else:
    	 		l = mid + 1
    
    	print(store)