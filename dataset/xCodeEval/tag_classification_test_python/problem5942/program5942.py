    from fractions import gcd
    input()
    arr = [int(x)-1 for x in input().strip().split()]
def foo(arr):
    	n = len(arr)
    	reverse = [None] * n
    	for i, c in enumerate(arr):
    		reverse[c] = i
    	for i in reverse:
    		if i is None:
    			return -1
    	result = 1
    	for i in xrange(n):
    		if arr[i] is None:
    			continue
    		ln = 1
    		b = arr[i]
    		arr[i] = None
    		while arr[b] is not None:
    			tmp = arr[b]
    			arr[b] = None
    			b = tmp
    			ln += 1
    		if ln % 2 == 0:
    			ln /= 2
    		result = result * ln / gcd(result, ln)
    	return result
    print(foo(arr))