def main():
    	n = input()
    	L = [int(x) for x in input().split()]
    	(boolean, lists) = solver(L)
    	print(boolean)
    	if boolean == 'YES':
    		print(len(lists))
    		for (l, r) in lists:
    			print(l, r)
    
def solver(L):
    	if L == [0] * len(L):
    		return ('NO', [])
    	else:
    		start = firstNonZero(L)
    		end = lastNonZero(L)
    		i = start
    		lists = []
    		#while i < end + 1:
    		total = sum(L[start:end+1])
    		if total != 0:
    			return ('YES', [(1, len(L)])
    		else:
    			return ('YES', [(1, end), (end + 1, len(L))])
    		# total = 0
    		# for j in range(i, end + 1):
    		# 	total += 
    
def firstNonZero(L):
    	for i in range(len(L)):
    		if L[i] != 0:
    			return i
    	assert(False)
    
def lastNonZero(L):
    	for i in range(len(L) - 1, -1, -1):
    		if L[i] != 0:
    			return i
    	assert(False)
    
    #print(solver([1, 2, 3, -5]))
    main()